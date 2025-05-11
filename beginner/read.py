import cv2 as cv

# img = cv.imread('photos/R.jpg')  
# cv.imshow('cat', img)



capture=cv.VideoCapture("photos/d.p4.mp4")

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()        
cv.destroyAllWindows()

cv.waitKey(0) 




