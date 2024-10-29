import cv2

cap = cv2.VideoCapture(0) 
# cv2.VideoCapture() is used to open a video file. Here, it's opening a file named 'Thomas Shelby 4K mega Twixtor _ #fypシ #twixtor #thomasshelby.mp4'.
# cap is the object that manages the video stream (reading frames, checking status, etc.).

if not cap.isOpened():                  # cap.isOpened() checks if the video file was opened successfully.
    print("Error: Could not open the video camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()