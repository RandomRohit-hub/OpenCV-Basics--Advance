import cv2 as cv
import numpy as np

# Read the image
img = cv.imread('photos/c.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found.")
    exit()

# Display the original image
cv.imshow('City', img)

# Function to translate an image
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# Translate the image
translated = translate(img, -100, 100)

# Display the translated image
cv.imshow('Translated', translated)


##rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # This part must run regardless of whether rotPoint was None
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# First rotation
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Second rotation on the rotated image
rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', rotated_rotated)




#resizing

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)



#flipping

flip=cv.flip(img,0)
cv.imshow('Flip',flip)


#croping

cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)




# Wait for a key press and close windows
cv.waitKey(0)
cv.destroyAllWindows()










