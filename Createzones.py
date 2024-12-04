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
- Press 'N' to be able to create another Polygon
- Press 'Space' to pause and draw another polygon

Features:
- Annotate video frames interactively by drawing a polygon.
- View real-time updates of the polygon on the video frames.
- Save and display the annotated points in the console.
"""

import cv2
import numpy as np

# Global variables
all_polygons = []  # List to store multiple polygons
current_polygon = []  # Points for the current polygon

# Read your video file
video_path = '/home/tim/optical_tr/distortion_correction/sample.mp4'
cap = cv2.VideoCapture(video_path)

# Callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    global current_polygon
    if event == cv2.EVENT_LBUTTONDOWN:
        current_polygon.append((x, y))
        print(f"Point Added to Current Polygon: (X: {x}, Y: {y})")

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

    # Draw all polygons on the frame
    for polygon in all_polygons:
        if len(polygon) > 1:
            cv2.polylines(frame, [np.array(polygon)], isClosed=True, color=(0, 255, 0), thickness=2)

    # Draw the current polygon
    if len(current_polygon) > 1:
        cv2.polylines(frame, [np.array(current_polygon)], isClosed=False, color=(255, 0, 0), thickness=2)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for a key press with a short delay
    key = cv2.waitKey(80)

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
    elif key == ord('n'):  # Press 'n' to finish the current polygon and start a new one
        if len(current_polygon) > 2:  # Only save polygons with at least 3 points
            all_polygons.append(current_polygon.copy())  # Append a copy of the current polygon
            print("Polygon completed and saved. Starting a new one.")
        else:
            print("Polygon must have at least 3 points.")
        current_polygon.clear()  # Clear current polygon for a fresh start

# Cleanup
cv2.destroyAllWindows()
cap.release()

# Print all collected polygons
print("All Polygons:")
for idx, polygon in enumerate(all_polygons, start=1):
    print(f"Polygon {idx}:")
    for point in polygon:
        print(f"  X: {point[0]}, Y: {point[1]}")
