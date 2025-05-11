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

# Wait for a key press and close windows
cv.waitKey(0)
cv.destroyAllWindows()










