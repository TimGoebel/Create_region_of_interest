"""
Interactive Polygon Drawer for Video Frames

This script allows users to interactively draw polygons on video frames using mouse clicks.
It is designed for applications like annotating regions of interest (ROIs) for computer vision tasks.

How to Use:
- Replace 'video_path' with the path to your video file.
- Run the script to load the video.
- Use the left mouse button to add points for the polygon.
- Press 'q' to quit the application.
- Press 'Space' to pause and resume the video.

Features:
- Annotate video frames interactively by drawing a polygon.
- View real-time updates of the polygon on the video frames.
- Save and display the annotated points in the console.
"""

import cv2
import numpy as np

# Global variables
polygon_points = []

# Read your video file
video_path = 'Your/diretory/sample.mp4'
cap = cv2.VideoCapture(video_path)

# Callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    global polygon_points
    if event == cv2.EVENT_LBUTTONDOWN:
        polygon_points.append((x, y))
        print(f"Point Added: (X: {x}, Y: {y})")

# Create a window and set the mouse callback
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse_callback)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        print("End of video reached.")
        break

    frame = cv2.resize(frame, (1443, 945))

    # Draw the polygon on the frame
    if len(polygon_points) > 1:
        cv2.polylines(frame, [np.array(polygon_points)], isClosed=False, color=(0, 255, 0), thickness=2)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for a key press with a short delay
    key = cv2.waitKey(80)  # Adjust delay (e.g., 20ms) for smoother operation

    if key == ord('q'):  # Press 'q' to exit
        print("Exiting.")
        break
    elif key == ord(' '):  # Press 'Space' to pause video and wait for next action
        print("Paused. Press 'Space' to resume or 'q' to quit.")
        while True:
            key = cv2.waitKey(0)
            if key == ord('q'):
                break
            elif key == ord(' '):
                print("Resuming playback.")
                break
        if key == ord('q'):
            break

# Cleanup
cv2.destroyAllWindows()
cap.release()

# Print the collected polygon points
print("Polygon Points:")
for point in polygon_points:
    print(f"X: {point[0]}, Y: {point[1]}")
