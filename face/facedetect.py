# pylint: disable=no-member

import cv2 as cv
import ctypes

# Function to get screen resolution (cross-platform)
def get_screen_resolution():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height

# Resize image to fit screen while keeping aspect ratio
def resize_to_fit_screen(img, max_width, max_height):
    h, w = img.shape[:2]
    scale = min(max_width / w, max_height / h)
    new_w, new_h = int(w * scale), int(h * scale)
    return cv.resize(img, (new_w, new_h), interpolation=cv.INTER_AREA)

# Load image
img = cv.imread('photos/gg.jpg')
if img is None:
    raise FileNotFoundError("Image not found at 'photos/gg.jpg'")

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Load Haar cascade
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
if haar_cascade.empty():
    raise FileNotFoundError("Failed to load Haar cascade classifier.")

# Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print(f'Number of faces found = {len(faces_rect)}')

# Draw rectangles
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# Resize image to screen resolution
screen_w, screen_h = get_screen_resolution()
img_resized = resize_to_fit_screen(img, screen_w, screen_h)

# Show result
cv.imshow('Detected Faces', img_resized)
cv.waitKey(0)
cv.destroyAllWindows()
