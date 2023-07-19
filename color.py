import cv2 as cv
import numpy as np
import os


def color_oranges(image_path):
    result = []

    # Read the image
    image = cv.imread(image_path)
    copy_img = image.copy()

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

    # Find contours in the binary mask
    contours, hierarchy = cv.findContours(mask_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    contour_area = []
    for contour in contours:
        area = cv.contourArea(contour)
        if area < 3000:
            continue
        contour_area.append(area)
        (x, y), (major_axis, minor_axis), angle = cv.fitEllipse(contour)
        ellipticity = major_axis / minor_axis
        perimeter = cv.arcLength(contour, True)

        # Calculate circularity as 4*pi*area/perimeter^2
        circularity = (4 * np.pi * area) / (perimeter * perimeter)

        # Define circularity and ellipticity thresholds based on requirements
        circularity_threshold = 0.99
        ellipticity_threshold = 0.90

        # If the contour's circularity and ellipticity are above the thresholds, consider it as an orange
        if circularity > circularity_threshold or ellipticity > ellipticity_threshold:
            # Create a mask for the contour
            mask = np.zeros_like(image)
            cv.drawContours(mask, [contour], -1, (255, 255, 255), -1)

            # Calculate mean values of a and b channels for pixels inside contour
            a_mean = np.mean(image[np.where(mask[..., 0] == 255)][..., 1])
            b_mean = np.mean(image[np.where(mask[..., 0] == 255)][..., 2])

            # Calculate CCI for the contour
            L = 100  # Reference illuminant
            CCI = 1000 * (a_mean / (L * b_mean))

            # Map the CCI value to the range of 0 to 99
            CCI = np.clip(CCI, -24, 22)
            CCI = (CCI + 24) * (99 / 46)

            # Draw the contour and the CCI value on the image
            cv.drawContours(image_copy, [contour], -1, (0, 255, 0), 2)
            # cv2.putText(image_copy, f'CCI: {CCI:.2f}', tuple(contour[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
            cv.putText(image_copy, f'CCI:{CCI:.2f}', tuple(contour[0][0]), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    return image_copy