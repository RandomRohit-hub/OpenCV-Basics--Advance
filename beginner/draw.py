import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# 1. Color a region (Optional - Uncomment to use)
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("Red Patch", blank)

# 2. Draw a rectangle (Optional - Uncomment to use)
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
# cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# Wait for key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()
