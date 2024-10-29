import cv2  
import time  

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit() 

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('saved\output.avi', fourcc, 20.0, (640, 480)) 


prev_frame_time = 0 
new_frame_time = 0  

while True:
    # Update the current frame's time ,calculating the time interval
    new_frame_time = time.time()
    
    # Capture each frame from the video
    ret, frame = cap.read()
    
    # Check if the frame was successfully captured
    if not ret:
        print("Error: Failed to capture frame.")
        break  

    # Write the captured frame to the output video
    out.write(frame)

    # Calculate FPS (Frames Per Second)
    fps = 1 / (new_frame_time - prev_frame_time)  # FPS = 1 / Time between frames
    prev_frame_time = new_frame_time  # Update the previous frame's time

    # Overlay the FPS text on the current frame
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Webcam', frame)

    # Print the FPS value to the console
    print(f"FPS: {int(fps)}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()
