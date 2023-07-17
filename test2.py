import cv2

# Load the video file
video = cv2.VideoCapture('path/to/video/file.mp4')

# Set the timestamps at which you want to take screenshots (in seconds)
timestamps = [1, 5, 10, 15]

# Loop through the timestamps
for timestamp in timestamps:
    # Set the position in the video to the current timestamp
    video.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)  # convert to milliseconds

    # Read the frame at the current position
    success, image = video.read()

    if success:
        # Save the screenshot image to a file with the timestamp in the filename
        cv2.imwrite(f'screenshot_{timestamp}s.png', image)