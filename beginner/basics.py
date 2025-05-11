import cv2 as cv

# Load the image
img = cv.imread('photos/R.jpg')
cv.imshow('Cat', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)
#cv.destroyAllWindows()




