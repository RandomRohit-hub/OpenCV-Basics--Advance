import cv2 as cv

# img = cv.imread('photos/R_small.jpg')  
# cv.imshow('cat', img)


def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# cv.waitKey(0)
#reading vid


capture=cv.VideoCapture("photos/d.p4.mp4")

while True:
    isTrue,frame=capture.read()


    frame_resize=rescale(frame,scale=.2)
   
   
   
    cv.imshow('Video',frame)
    cv.imshow('video resized ',frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()        
cv.destroyAllWindows()

cv.waitKey(0) 
