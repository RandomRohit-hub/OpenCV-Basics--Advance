import cv2 as cv
img=cv.imread('photos/c.jpg')
cv.imshow('City',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# canny=cv.Canny(img,125,125)
# cv.imshow('Canny Edges',canny)

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('BLUR',blur)

# contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours(s) found!')




ret,thresh=cv.threshold(gray,125,125,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)








contours,heirarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours(s) found!')






cv.waitKey(0)
cv.destroyAllWindows()