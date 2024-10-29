# Import NumPy for handling arrays
import cv2 
import numpy as np

# Read the image in grayscale mode (0 means grayscale). The image is stored in the 'img' variable
img = cv2.imread('image1.jpeg', 0)

# Create a kernel (structuring element) of size 5x5 with all values set to 1
# This kernel will be used for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply morphological 'opening' on the image using the kernel
# Opening = Erosion followed by Dilation, which helps in removing small noise
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Apply morphological 'closing' on the image using the same kernel
# Closing = Dilation followed by Erosion, which helps in filling small gaps or holes
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display the result of the opening operation in a window labeled 'Opening (Noise Removal)'
cv2.imshow('Opening (Noise Removal)', opening)

# Display the result of the closing operation in a window labeled 'Closing (Fill Gaps)'
cv2.imshow('Closing (Fill Gaps)', closing)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all the OpenCV windows opened by the program
cv2.destroyAllWindows()

