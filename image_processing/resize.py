import cv2

img = cv2.imread('image1.jpeg')
resized = cv2.resize(img, (200, 200))
#(new width in pixels,new height in pixels)
 
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()