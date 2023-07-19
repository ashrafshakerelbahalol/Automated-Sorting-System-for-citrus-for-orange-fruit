import cv2 as cv
import numpy as np
import cv2

def background_removel(image_path):
    image = cv.imread(image_path)
    copy_img = image

    # Convert the image to the HSV color space
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define the color range for orange and green in the HSV space
    lower_orange_and_green = np.array([0, 40, 40])
    upper_orange_and_green = np.array([70, 255, 255])

    hsv_copy = image.copy()

    # Threshold the image to get a binary mask
    mask = cv.inRange(hsv, lower_orange_and_green, upper_orange_and_green)

    # Find contours in the binary mask
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Filter the contours based on area
    filtered_contours = [contour for contour in contours if cv.contourArea(contour) >= 500]

    # Apply convex hull to the filtered contours
    hull_contours = [cv.convexHull(contour) for contour in filtered_contours]

    # Create a mask with only the hull contours
    mask_2 = np.zeros_like(hsv, dtype=np.uint8)
    mask_2 = cv.cvtColor(mask_2, cv.COLOR_BGR2GRAY)
    cv.drawContours(mask_2, hull_contours, -1, (255, 255, 255), thickness=cv.FILLED)

    # Apply the mask to the image
    image_copy = cv.bitwise_and(image, image, mask=mask_2)

    # Draw index number in the center of each contour
    for i, contour in enumerate(filtered_contours):
        M = cv.moments(contour)
        if M["m00"] == 0:
            continue
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.putText(image_copy, str(i + 1), (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 200, 0), 4)

    return image_copy


