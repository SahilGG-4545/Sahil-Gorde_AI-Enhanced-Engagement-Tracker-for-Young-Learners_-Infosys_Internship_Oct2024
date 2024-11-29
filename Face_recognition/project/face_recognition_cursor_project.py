import cv2 as cv
import face_recognition
import dlib
import pandas as pd
import numpy as np
from datetime import datetime
import os
from imutils import face_utils
import time
from datetime import timedelta

# Initialize dlib's face detector and the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(p)

# Create a directory to save screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Load the known image of Barack Obama
known_image = face_recognition.load_image_file("sahil.jpg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Create a DataFrame to store recognized face information
columns = ['Name', 'Date', 'Time', 'Screenshot', 'Attentive', 'Attention Score', 
          'Posture', 'Head Movement', 'Session Duration', 'Attentive Duration']
df = pd.DataFrame(columns=columns)

# Launch the live camera or video
cam = cv.VideoCapture(0)
print("Camera")
if not cam.isOpened():
    print("Camera not working")
    exit()

# Define the maximum thresholds for yaw, pitch, and roll beyond which attentiveness is 0
MAX_YAW_THRESHOLD = 0.5
MAX_PITCH_THRESHOLD = 0.5
MAX_ROLL_THRESHOLD = 0.5
POSTURE_THRESHOLD = 0.15  # Threshold for vertical head position
MIN_BRIGHTNESS = 0.2
MAX_BRIGHTNESS = 0.8

# Helper function for detecting head pose
def get_head_pose(landmarks):
    image_points = np.array([
        landmarks[30],  # Nose tip
        landmarks[8],   # Chin
        landmarks[36],  # Left eye left corner
        landmarks[45],  # Right eye right corner
        landmarks[48],  # Left mouth corner
        landmarks[54]   # Right mouth corner
    ], dtype="double")
    
    model_points = np.array([
        (0.0, 0.0, 0.0),             # Nose tip
        (0.0, -330.0, -65.0),        # Chin
        (-165.0, 170.0, -135.0),     # Left eye left corner
        (165.0, 170.0, -135.0),      # Right eye right corner
        (-150.0, -150.0, -125.0),    # Left mouth corner
        (150.0, -150.0, -125.0)      # Right mouth corner
    ])
    
    focal_length = 320
    center = (160, 120)  # Adjusted for 320x240 resolution
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]], dtype="double")
    
    dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
    success, rotation_vector, translation_vector = cv.solvePnP(model_points, image_points, camera_matrix, dist_coeffs)
    
    return rotation_vector, translation_vector

# Function to calculate attentiveness score between 0 and 1 based on yaw and pitch
def calculate_attention_score(yaw, pitch):
    yaw_score = max(0, 1 - abs(yaw[0]) / MAX_YAW_THRESHOLD)
    pitch_score = max(0, 1 - abs(pitch[0]) / MAX_PITCH_THRESHOLD)
    # Overall score as the average of yaw and pitch scores
    attention_score = (yaw_score + pitch_score) / 2
    return attention_score

# Add these new helper functions before the main loop
def analyze_posture(landmarks, frame_height):
    """Analyze if person is slouching based on nose position"""
    nose_bridge = landmarks[27]  # Nose bridge point
    relative_height = nose_bridge[1] / frame_height
    return relative_height < POSTURE_THRESHOLD

def adjust_brightness(frame):
    """Automatically adjust frame brightness and contrast"""
    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    l, a, b = cv.split(lab)
    
    # Apply CLAHE to L channel
    clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    
    # Merge channels
    merged = cv.merge((cl,a,b))
    return cv.cvtColor(merged, cv.COLOR_LAB2BGR)

def analyze_head_movement(rotation_vector):
    """Analyze head movements for nodding and shaking"""
    yaw, pitch, roll = rotation_vector
    
    head_state = "neutral"
    if abs(pitch[0]) > 0.3:  # Nodding threshold
        head_state = "nodding" if pitch[0] > 0 else "looking_down"
    elif abs(yaw[0]) > 0.3:  # Shaking threshold
        head_state = "shaking"
    
    return head_state

# Add these variables before the main loop
session_start = time.time()
last_attentive_time = time.time()
total_attentive_time = 0

frame_count = 0
try:
    while True:
        frame_count += 1
        ret, frame = cam.read()
        
        if not ret:
            print("Can't receive frame")
            break

        if frame_count % 2 == 0:  # Skip every other frame
            continue

        frame = cv.resize(frame, (320, 240))  # Downscale for faster processing
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces in the current frame
        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            continue

        # Encode faces for comparison
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Add brightness adjustment after frame capture
        frame = adjust_brightness(frame)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Calculate distance from known face
            distance = face_recognition.face_distance([known_faces], face_encoding)[0]

            if distance < 0.6:
                # Recognized as Barack Obama
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                name = 'Sahil Gorde'
                
                # Landmark detection for attentiveness analysis
                face_landmarks = landmark_predictor(gray, dlib.rectangle(left, top, right, bottom))
                landmarks = [(p.x, p.y) for p in face_landmarks.parts()]
                
                # Draw green circles on each facial landmark
                for (x, y) in landmarks:
                    cv.circle(frame, (x, y), 2, (0, 255, 0), -1)

                # Calculate head pose and attention score
                rotation_vector, translation_vector = get_head_pose(landmarks)
                yaw, pitch, roll = rotation_vector
                attention_score = calculate_attention_score(yaw, pitch)
                
                # Analyze posture
                good_posture = analyze_posture(landmarks, frame.shape[0])
                posture_status = "Good" if good_posture else "Poor"
                
                # Analyze head movement
                head_movement = analyze_head_movement(rotation_vector)
                
                # Update attention duration
                current_time = time.time()
                if attention_score >= 0.5:
                    total_attentive_time += current_time - last_attentive_time
                last_attentive_time = current_time
                
                session_duration = current_time - session_start
                
                # Set attentive to 'Yes' if attention score >= 0.5, else 'No'
                attentive = 'Yes' if attention_score >= 0.5 else 'No'

                # Save screenshot if attentive and display score on frame
                screenshot_filename = f"screenshots/{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                if attentive == 'Yes':
                    cv.putText(frame, f'Attentive (Score: {attention_score:.2f})', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
                else:
                    cv.putText(frame, f'Not Attentive (Score: {attention_score:.2f})', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

                # Log the recognition event with attentiveness score
                cv.imwrite(screenshot_filename, frame)  # Save screenshot
                new_entry = pd.DataFrame({
                    'Name': [name],
                    'Date': [now.strftime("%Y-%m-%d")],
                    'Time': [now.strftime("%H:%M:%S")],
                    'Screenshot': [screenshot_filename],
                    'Attentive': [attentive],
                    'Attention Score': [attention_score],
                    'Posture': [posture_status],
                    'Head Movement': [head_movement],
                    'Session Duration': [str(timedelta(seconds=int(session_duration)))],
                    'Attentive Duration': [str(timedelta(seconds=int(total_attentive_time)))]
                })
                df = pd.concat([df, new_entry], ignore_index=True)

                # Draw rectangle and label around the face
                cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0) if attentive == 'Yes' else (0, 0, 255), 2)
                cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv.LINE_AA)

                # Display additional information on frame
                cv.putText(frame, f'Posture: {posture_status}', (10, 60), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                cv.putText(frame, f'Movement: {head_movement}', (10, 90), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                cv.putText(frame, f'Attentive Time: {int(total_attentive_time)}s', (10, 120), 
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # Display the frame
        cv.imshow("Video Stream", frame)
        if cv.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if not df.empty:
        # Calculate and print session summary
        total_duration = time.time() - session_start
        attention_percentage = (total_attentive_time / total_duration) * 100 if total_duration > 0 else 0
        
        print("\nSession Summary:")
        print(f"Total Duration: {str(timedelta(seconds=int(total_duration)))}")
        print(f"Attentive Duration: {str(timedelta(seconds=int(total_attentive_time)))}")
        print(f"Attention Percentage: {attention_percentage:.2f}%")
        
        df.to_excel('atten_score.xlsx', index=False)
        print("\nAttendance with attentiveness saved to 'atten_score.xlsx'.")
    
    cam.release()
    cv.destroyAllWindows()
