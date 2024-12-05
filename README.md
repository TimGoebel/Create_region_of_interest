# Interactive Polygon Drawer for Video Frames

This Python script allows users to interactively draw **multiple polygons** on video frames using the mouse and view the results in real-time. It is useful for applications like annotating regions of interest (ROIs) in videos for computer vision tasks.

## Features
- Load a video file for annotation.
- Use the mouse to add points to form polygons.
- Real-time drawing of polygons on the video frames.
- Create and manage **multiple polygons** using intuitive controls.
- **Pause and resume video playback** using the **Space** key (drawing allowed only while paused).
- **Undo** the last point added to the current polygon with the **U** key.
- Save the current polygon and start a new one using the **N** key.
- **Quit** the application using the **Q** key.
- Display all collected polygon points at the end of the session.
- **Save the polygons** as a JSON file for further use.

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
   python3 Createzones.py
   ```
2. **Annotate**:
   - Use **Left Mouse Click** to add points for the current polygon **while the video is paused**.
   - Press **N** to save the current polygon and start a new one.
   - Press **U** to undo the last point added to the current polygon.
   - All polygons will be displayed on the video frames when the video is resumed.
3. **Controls**:
   - Press **Q** to quit.
   - Press **Space** to toggle between pause and resume (drawing is only allowed when paused).
4. **Save Polygons**:
   - After finishing annotation, the polygons are automatically saved to a **JSON file**.
   - The JSON file contains all the polygon data, which can be used for future processing.

---

## Code Overview

### Key Components
- **Mouse Callback**: Adds points to the current polygon when the left mouse button is clicked, but only when the video is paused.
- **Pause/Resume**: The **Space** key is used to pause and resume video playback. While paused, users can draw polygons. 
- **Multiple Polygon Management**: Save the current polygon and begin a new one using the **N** key.
- **Undo Functionality**: Use the **U** key to undo the last point added to the current polygon while paused.
- **Video Playback**: Displays video frames in a resizable window.
- **Polygon Drawing**: Dynamically renders each polygon as points are added, but only when the video is paused.
- **JSON Saving**: The polygon data is saved to a `polygons.json` file at the end of the session.

### Example Output
The console prints the polygon points in the format:
```
Point Added: (X: 100, Y: 200)
Polygon Completed:
X: 100, Y: 200
X: 150, Y: 250
...
```

### JSON File Format
The polygons are saved as a JSON file in the following format:
```json
[
    [[100, 200], [150, 250], [200, 200], ...],
    [[300, 400], [350, 450], [400, 400], ...],
    ...
]
```
Each polygon is represented as an array of points, and all polygons are stored in a list.

---

## Future Enhancements
- Add functionality to save the polygon data to a file.
- Support for drawing closed polygons by default.
- Add support for exporting the video with annotated polygons.

---

## License
This project is licensed under the MIT License.

---

Enjoy annotating your videos with multiple regions of interest! 🎥
