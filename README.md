# Sahil-Gorde_AI-Enhanced-Engagement-Tracker-for-Young-Learners_-Infosys_Internship_Oct2024
## Image Processing
### Libraries or Frameworks Used
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

### Developed Logics:

#### A) Image Concatenation
Resizes two images to a specified pixel range and merges them both horizontally and vertically, displaying the results in separate windows.
- **Input**:
  <br>
   <img src="https://github.com/user-attachments/assets/488a9a57-3ead-4da9-ac7a-c586b4f9d6a9" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/1499a03e-3496-447c-95eb-cb59248586d3" alt="concat" >


#### B) Image Contour Detection
Identifies contours in a grayscale image using a binary threshold and `cv2.findContours()`. Draws these contours on the original image in green.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/dc9fc404-2834-4444-a72b-bcca7013123e" alt="concat" >

#### C) Image Cropping
Extracts and displays a defined region of an image based on specified pixel coordinates.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/024e0b9a-63e5-4a88-a20b-594eea153fe6" alt="concat" >
#### D) Image Dilation & Erosion
Performs morphological operations to enlarge and shrink image features, enhancing and reducing specific areas respectively.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/b8e6db86-6068-456a-9016-80b7b9c2b57f" alt="concat" >

#### E) Edge Detection
Uses the Canny edge detection algorithm to highlight edges within a grayscale image.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/c26bbde4-a0b7-41a7-9baa-8a92a08e2737" alt="concat" >

#### F) Histogram Equalization
Improves the contrast of a grayscale image through histogram equalization.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/2fa2b140-0bc0-441d-bb7c-a27e3139ebc1" alt="concat" >

#### G) HSV Conversion
Converts a color image from the BGR format to the HSV color space.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/a870db5e-b6a9-4087-86f5-0df84d317143" alt="concat" >

#### H) Morphological Transformations
Applies opening and closing operations on a grayscale image to minimize noise and fill small gaps.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/0cd0e1c2-b376-436d-9013-76230b042590" alt="concat" >


#### I) Image Resizing
Adjusts the dimensions of an image according to specified width and height.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/9b5c1da2-5b12-4178-b447-fb9462efe1a6" alt="concat" >

#### J) RGB to Grayscale Conversion
Transforms a color image to a grayscale representation.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/d82d2fc3-3312-4059-a4ae-4a3b28f6260d" alt="concat" >

#### K) Image Rotation
Rotates an image 90 degrees around its center point.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/e9856754-fca9-4b09-82fc-02fed03df3d2" alt="concat" >

#### L) Image Blurring
Applies a Gaussian blur to an image to reduce noise and soften details.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/42e5dc7e-fb6c-4fd6-8d65-f7b3f4cb6666" alt="concat" >

#### M) Template
This function performs template matching to locate a template image within a larger image.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/375edbaf-4e30-48d0-a8cc-df1348bfe16a" alt="concat" >
#### N) image_noise_removal & closing_gaps
Removes noise and closes gaps in an image using morphological operations.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/95509430-7e72-4b07-b985-bebab9ae09cb" alt="concat" >
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/45331561-a398-42fd-9139-70ab4c96eace" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/e0b3bd6f-d68d-4dc6-a5bb-8fa263061576" alt="concat" width="400" style="margin-right: 20">

## Video Processing

### Libraries and Frameworks Utilized
- **OpenCV**: Version 4.10.0.84 

### Developed Logics:

#### A) Video_multivideo
Reads and showcases images from a given directory, printing the dimensions of each image to the console for batch image analysis.

#### B) Video_fps
A real-time video capture function that displays a live video feed while calculating and showing the frames per second (FPS) for performance monitoring.

#### C) Video_save
Captures live video from the webcam and writes it to a specified output file, allowing easy recording and saving of video content.

#### D) Video_stack
Reads two separate video files, resizes them, and combines them side by side for synchronized dual-video playback, ideal for comparing footage.

#### E) Video_stream
Captures and streams live video feed from the webcam, displaying it in real-time. Useful for basic video streaming applications.

## Annotations Project Overview

### Libraries and Frameworks Utilized
- **OpenCV**: Version 4.10.0.84 for advanced image processing
- **LabelImg**: Version 1.8.6 for image annotation

### Developed Logics:

#### A) data_segregate
Organizes images and label files into separate directories for matched and unmatched pairs, aiding in dataset preparation for ML projects.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/f2b358cf-261e-47de-86d9-e04096c421ac" alt="concat" width="400" style="margin-right: 20">
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/a0b7f7b0-9e0c-447b-a261-ad0642b266fc" alt="concat" width="400" style="margin-right: 20">   <img src="https://github.com/user-attachments/assets/180c5f6b-a40c-46f2-ac49-8ed0a74644da" alt="concat" width="400" style="margin-right: 20">

#### B) label
Draws bounding boxes on images based on annotation data, useful for visualizing object detection outcomes.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/d2f07d2e-28c6-432e-b069-450117a8f2c3" alt="concat">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/4142b215-f5b5-4d9f-8f58-a93fc7916526" alt="concat" >

#### C) label_manipulate
Updates class numbers within label files, enabling easy reclassification in object detection tasks.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/a7d278a2-0273-4132-bda3-6551733cc2e3" alt="concat" width="400" style="margin-right: 20">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/0fec7f48-512a-493a-aae1-18e033216a87" alt="concat" width="400" style="margin-right: 20">   <img src="https://github.com/user-attachments/assets/bd51289a-aaa8-419c-87f6-728220d6d130" alt="concat" width="400" style="margin-right: 20">

## Face Recognition Project

### Libraries or Frameworks Used
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) Face_recognition

This program utilizes live video streaming to identify "Sahil Gorde" through face recognition and provide instant feedback.
1. **Loading and Encoding Reference Data**: A stored image of "Sahil Gorde" is processed and encoded into a set of facial features, serving as a reference for real-time comparison. 
2. **Camera Initialization**:The program accesses the webcam to capture live video frames for face detection and recognition tasks.  
3. **Face Matching Logic**: Detected faces in the video are encoded, and their similarity to the reference encoding is measured. A match is confirmed if the calculated distance is below the confidence threshold (0.6).  
4. **Real-Time Annotation**: Matched faces are marked with a green rectangle and labeled "Sahil," while unmatched faces are displayed with "Not Sahil" for clarity.  
5. **Live Feedback Loop**:The program displays the annotated video feed in real time and stops processing when 'q' is pressed.
   
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat"  width="400" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/0811adff-cec4-4f51-940e-e1a5ee6d496b" alt="concat" width="400" style="margin-right: 20">
#### B) Attendence_save

This program uses real-time face recognition to track and record attendance via a webcam. It saves recognized face details in an Excel file after detecting a set number of matches.

1. **Loading Known Face**: Loads a known image and extracts facial encodings for comparison.
2. **Camera Initialization**: Captures video from the webcam, processing every second frame to improve performance.
3. **Face Detection and Recognition**: Detects faces in each frame and compares them with the known face encoding. If a match is found, it draws a rectangle around the face and labels it.
4. **Attendance Recording**: If recognized, the name, date, and time are recorded in a DataFrame (`df`). After 5 recognitions, the data is saved to an Excel file (`attendence_Save.xlsx`) and the counter resets.
5. **Real-time Display**: The processed video stream is displayed with face bounding boxes, and "Not Recognized" is shown if no match is found.
6. **Termination**: The video feed stops when the 'q' key is pressed, and any remaining data is saved to the Excel file before the program ends.


- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat"  width="400">
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/0e91cca2-7720-4094-8374-e59a1e458d94" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/7ca9fea8-09a5-43aa-9716-76ef24c30e3d" alt="concat" width="400" style="margin-right: 20">
  
#### C) test
This program tracks and logs face recognition in real-time while managing duplicate entries.

1. **Initialization**: Sets up known face encodings, logging DataFrame, and camera capture.  
2. **Frame Processing**: Skips frames for optimized performance and detects faces in the live video.  
3. **Recognition Logic**: Identifies "Sahil" based on proximity to known face encodings and draws labels.  
4. **Time-Based Entry Rules**: Ensures duplicate entries are avoided unless a 5-minute gap occurs.  
5. **Automatic Data Storage**: Periodically saves attendance logs to an Excel file every 30 seconds.  
6. **Error Handling and Cleanup**: Safely handles exceptions, saves logs, and releases resources on exit. 
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400" >
- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/bade3f80-1aab-47ad-9f8e-296e1d4d269c" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/823edc07-7930-4f82-98d2-b125610576ba" alt="concat" width="400" style="margin-right: 20">
#### D) tools
This program identifies and logs the presence of a specific individual, "Sahil," in real-time.

1. **Face Recognition Initialization**: Encodes a known face image for comparison in live video feed.  
2. **Live Camera Feed**: Captures frames while skipping every second frame to optimize processing.  
3. **Real-Time Face Detection**: Detects faces and identifies Sahil using a confidence threshold.  
4. **Dynamic Data Logging**: Saves recognition details (name, date, time) to an Excel file after five detections.  
5. **On-Screen Labels**: Displays labels "Sahil" or "Not Sahil" based on recognition results in the video feed.  
6. **Final Data Storage**: Ensures attendance data is saved when the program exits.  
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400">
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/d4b5b22f-3efe-46b2-a0ba-28012cdb44c7" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/13adc74e-1840-4179-b07b-922eb65ceb1e" alt="concat" width="400" style="margin-right: 20">
#### E) excel_sc

This program recognizes a specific person (e.g., "Sahil Gorde") using face recognition and logs the details along with screenshots at set intervals.
1. **Face Recognition**: Detects faces and compares them with a known image.
2. **Screenshot Capture**: Saves screenshots of recognized faces at defined intervals (every 2 minutes or after a 5-minute gap).
3. **Data Logging**: Logs recognition data (name, date, time, screenshot path) in an Excel file.
4. **Efficiency**: Processes every other frame to reduce CPU usage.
5. **Face Labeling**: Labels recognized faces as "Sahil" and others as "Not Sahil".
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400" >
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/bd050cbe-2b43-4483-acd5-891588f5f0d6" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/bb49ffb5-265c-47e9-8e20-55dcc2f2b1ee" alt="concat" width="400" style="margin-right: 20">
#### F) excel_sc_dt

This program captures webcam video, performs real-time face recognition for "Sahil Gorde," saves screenshots, and logs attendance details into an Excel file.
1. **Face Detection and Encoding**:Loads a pre-saved image of "Sahil Gorde," encodes it, and compares it with faces detected in the live webcam feed.  
2. **Recognition Logic**:Uses a confidence threshold to determine if the detected face matches the known encoding. Faces are recognized and logged every 2 minutes, with a 5-minute gap for repeat entries.  
3. **Screenshot Saving**:Captures screenshots of recognized faces with the current date and time, overlays the timestamp, and stores them in a dedicated directory (`screenshots`).  
4. **Attendance Logging**:Logs recognition details, including name, date, time, and screenshot file path, into an Excel file (`excel_sc_dt.xlsx`) for easy access.  
5. **Real-Time Feedback**:Displays a live video feed with bounding boxes around detected faces, labeling recognized faces as "Sahil" and others as "Not Sahil."  
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat"  width="400">
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/ed12e6a8-85b2-4486-a51d-cb97c943b9d8" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/0cdc0daa-1e31-473f-934e-e42bb1f5d41c" alt="concat" width="400" style="margin-right: 20">
#### G) landmark
This program combines face recognition, facial landmark detection, and attentiveness analysis to monitor real-time behavior.

1. **Setup**: Initializes facial detection, landmark predictor, and loads "Sahil's" face encoding.  
2. **Camera Stream**: Captures live video, processing alternate frames for efficiency.  
3. **Face Recognition**: Matches detected faces with "Sahil" based on encoding distance.  
4. **Attentiveness Analysis**: Calculates head pose and evaluates attentiveness using yaw and pitch.  
5. **Logging**: Saves screenshots and logs recognition details in an Excel file (`landmark.xlsx`).  
6. **Display and Cleanup**: Shows live feedback and terminates with 'q', releasing resources and saving logs.
7. 
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400" >
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/62e7c3d3-624c-46b0-8054-9265a56e8733" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/67b72586-5011-4537-b6cf-562d8f50ebd3" alt="concat" width="400" style="margin-right: 20">
#### H) atten_score
This program uses real-time face recognition and head pose analysis to evaluate attentiveness based on yaw and pitch. It saves the details of the recognized face, attentiveness score, and screenshots in an Excel file and a designated folder.

1. **Face Recognition**: Detects and matches faces with a known image.
2. **Head Pose Analysis**: Calculates yaw and pitch to assess attentiveness.
3. **Attentiveness Score**: Computes a score based on head pose to determine if the person is attentive.
4. **Screenshot Capture**: Saves a screenshot if the person is attentive.
5. **Data Logging**: Records recognition details and attentiveness in an Excel file.

- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400" >
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/b5f07bf2-924b-46f3-a53a-e243b7e04afe" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/ec597cfe-8672-49be-85d8-a924db844cfb" alt="concat" width="400" style="margin-right: 20">
#### I) avg_atten_score
This program uses face recognition and head pose analysis to evaluate attentiveness, saving the results in an Excel file with average attention scores.

1. **Face Recognition**: Matches faces against a known image (e.g., Barack Obama).
2. **Head Pose Analysis**: Detects head yaw and pitch to evaluate attentiveness.
3. **Attentiveness Score**: Calculates an attention score based on head orientation.
4. **Screenshot Capture**: Saves screenshots when the user is attentive.
5. **Data Logging**: Logs recognition and attentiveness data into an Excel file.
6. **Average Score**: Computes and logs the average attentiveness score over time.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/bcbaf22b-ace0-4794-a299-b3db04b82e01" alt="concat" width="400" >
- **Output**:
  <br>
   <img src="https://github.com/user-attachments/assets/7e73ba36-d297-4c5d-b7ad-60209bfedd2c" alt="concat" width="400" style="margin-right: 20"> <img src="https://github.com/user-attachments/assets/f10096e4-a026-401c-86e7-00bfdf62d2d0" alt="concat" width="400" style="margin-right: 20">
