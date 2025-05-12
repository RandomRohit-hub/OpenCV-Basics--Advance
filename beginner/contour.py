import cv2 as cv
img=cv.imread('photos/c.jpg')
cv.imshow('City',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


canny=cv.Canny(img,125,125)
cv.imshow('Canny Edges',canny)



contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)


cv.waitKey(0)
cv.destroyAllWindows()