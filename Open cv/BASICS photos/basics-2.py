import cv2

earth = cv2.imread('earth.jpg')
cv2.imshow('window_name',earth)
#wait key zero means infinite time and we want to destroy the window by clicking
cv2.waitKey(300)
cv2.destroyAllWindows()

'''converting an image in the gray scale image'''
gray_earth = cv2.imread('earth.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray-earth',gray_earth)
cv2.waitKey(400)
cv2.destroyAllWindows()