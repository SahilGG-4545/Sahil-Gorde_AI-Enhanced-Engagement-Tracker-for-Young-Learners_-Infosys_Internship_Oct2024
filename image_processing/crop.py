import cv2

img = cv2.imread('image1.jpeg')
cropped = img[50:200, 100:300]
# img[vertical range,horizotal range]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()