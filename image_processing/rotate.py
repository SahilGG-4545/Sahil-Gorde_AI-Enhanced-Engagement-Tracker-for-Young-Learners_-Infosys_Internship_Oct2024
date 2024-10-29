import cv2

img = cv2.imread('image1.jpeg')

# Get the dimensions of the image (height and width)
# 'shape[:2]' extracts the height and width of the image and ignores the 3rd parameter rgb channel
(h, w) = img.shape[:2]

# Define the center of the image, which will be used as the center of rotation
# This is calculated by dividing the width and height by 2 (center of the image)
center = (w // 2, h // 2)

# Create a rotation matrix using OpenCV's 'getRotationMatrix2D' function
# Parameters: center of rotation, rotation angle (45 degrees), scale factor (1.0 for no scaling)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Apply the rotation to the image using the 'warpAffine' function
# Parameters: original image, rotation matrix, output image size (same as original)
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Rotated Image', rotated)

cv2.waitKey(0)

cv2.destroyAllWindows()
