# Interactive Polygon Drawer for Video Frames

This Python script allows users to interactively draw polygons on video frames using the mouse and view the results in real-time. It is useful for applications like annotating regions of interest (ROIs) in videos for computer vision tasks.

## Features
- Load a video file for annotation.
- Use the mouse to add points to form a polygon.
- Real-time drawing of the polygon on the video frames.
- Pause and resume playback using the **Space** key.
- Quit the application using the **Q** key.
- Display all collected polygon points at the end of the session.

---

## Getting Started

### Prerequisites
- Python 3.x
- OpenCV library (`cv2`)
- NumPy library (`numpy`)

You can install the required libraries using pip:
```bash
pip install opencv-python-headless numpy
```

### Installation
1. Clone this repository or download the script.
2. Replace `video_path` with the path to your video file.

---

## Usage

1. **Run the script**:
   ```bash
   python interactive_polygon_drawer.py
   ```
2. **Annotate**:
   - Use **Left Mouse Click** to add points for the polygon.
   - The points will be displayed as the polygon is drawn.
3. **Controls**:
   - Press **Q** to quit.
   - Press **Space** to pause/resume playback.

---

## Code Overview

### Key Components
- **Mouse Callback**: Adds points to the polygon when the left mouse button is clicked.
- **Video Playback**: Displays video frames in a resizable window.
- **Polygon Drawing**: Dynamically renders the polygon as points are added.

### Example Output
The console prints the polygon points in the format:
```
Point Added: (X: 100, Y: 200)
Polygon Points:
X: 100, Y: 200
X: 150, Y: 250
...
```

---

## Future Enhancements
- Add functionality to save the polygon data to a file.
- Support for drawing closed polygons.
- Add undo functionality to remove the last point.

---

## License
This project is licensed under the MIT License.

---

Enjoy annotating your videos! 🎥
