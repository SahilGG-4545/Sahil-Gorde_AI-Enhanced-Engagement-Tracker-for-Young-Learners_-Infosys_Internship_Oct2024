import cv2

image = cv2.imread("image1.jpeg")

# Convert the image from BGR (Blue, Green, Red) color format to Grayscale
# BGR is OpenCV's default format for color images
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image to the specified file path, overwriting the original image
cv2.imwrite("images\photo.jpeg", gray_image)

cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)

# Close all OpenCV windows that were opened during execution
cv2.destroyAllWindows()

