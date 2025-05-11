import cv2 as cv

# Load the image
img = cv.imread('photos/c.jpg')
cv.imshow('Cat', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#cv.destroyAllWindows()

#blur an image

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

## create an edge cascade
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)


#Dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)


#enroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

##resize
resize=cv.resize(img,(500,500))
cv.imshow('Resize',resize)



#cropping
crop=img[50:200,200:400]
cv.imshow('Cropped',crop)









cv.waitKey(0)