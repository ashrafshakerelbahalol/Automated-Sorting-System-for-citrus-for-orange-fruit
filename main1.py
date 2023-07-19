from background import background_removel
from detect import detection_oranges
from size import size_oranges
from color import color_oranges
from automatic import automtic_oranges
import cv2 as cv
import numpy as np

# Provide the path to the image
image_path = '3.bmp'

# Process the image and get the modified image
image_copy = color_oranges(image_path)

cv.imshow('Annotated Image', image_copy)
cv.waitKey(0)
cv.destroyAllWindows()