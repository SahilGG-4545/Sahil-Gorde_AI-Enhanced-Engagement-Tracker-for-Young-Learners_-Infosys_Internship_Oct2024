# Sahil-Gorde_AI-Enhanced-Engagement-Tracker-for-Young-Learners_-Infosys_Internship_Oct2024
## Image Processing
### Libraries or Frameworks Used
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

### Developed Logics

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

## Video Processing Project Overview

### Libraries and Frameworks Utilized
- **OpenCV**: Version 4.10.0.84 

### Developed Functionalities

#### A) Video_multivideo
Reads and showcases images from a given directory, printing the dimensions of each image to the console for batch image analysis.
- **Input**:
- **Output**:

#### B) Video_fps
A real-time video capture function that displays a live video feed while calculating and showing the frames per second (FPS) for performance monitoring.
- **Input**:
- **Output**:

#### C) Video_save
Captures live video from the webcam and writes it to a specified output file, allowing easy recording and saving of video content.
- **Input**:
- **Output**:

#### D) Video_stack
Reads two separate video files, resizes them, and combines them side by side for synchronized dual-video playback, ideal for comparing footage.
- **Input**:
- **Output**:

#### E) Video_stream
Captures and streams live video feed from the webcam, displaying it in real-time. Useful for basic video streaming applications.
- **Input**:
- **Output**:

## Annotations Project Overview

### Libraries and Frameworks Utilized
- **OpenCV**: Version 4.10.0.84 for advanced image processing
- **LabelImg**: Version 1.8.6 for image annotation

### Developed Functionalities

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
  <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/dc9fc404-2834-4444-a72b-bcca7013123e" alt="concat" >

#### C) label_manipulate
Updates class numbers within label files, enabling easy reclassification in object detection tasks.
- **Input**:
  <br>
  <img src="https://github.com/user-attachments/assets/7a649422-b004-493b-b602-5333a2cf9d21" alt="concat" width="400" style="margin-right: 20">

- **Output**:
  <br>
  <img src="https://github.com/user-attachments/assets/dc9fc404-2834-4444-a72b-bcca7013123e" alt="concat" >

## Face Recognition Project

### Libraries or Frameworks Used
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics

#### A) Face_recognition
#### B) Attendence_save
#### C) test
#### D) tools
#### E) excel_sc
#### F) excel_sc_dt
#### G) landmark
#### H) atten_score
#### I) avg_atten_score

