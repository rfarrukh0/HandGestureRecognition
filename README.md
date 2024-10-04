
# HandAI - Hand Gesture Recognition and Control

**HandAI** is a Python-based hand gesture recognition system that allows you to control various aspects of your computer using simple hand gestures. Currently, the application controls system volume through an "open palm" gesture. Future updates will add more gestures to enhance the user experience, such as playback control, workspace switching, and more.

## Features

- **Real-time hand gesture recognition**: Uses OpenCV and MediaPipe to detect hand gestures via your webcam.
- **System volume control**: Increase the system volume with an "open palm" gesture.
- **Real-time FPS display**: View the frames-per-second (FPS) on the live video feed.
- **Live gesture display**: The detected hand gesture is displayed on the video feed.

## Planned Features

This project is a work in progress. Future versions will include additional gestures and system control features:
- **Playback control**: Control media playback (play/pause, next/previous) with gestures.
- **Workspace switching**: Quickly switch between virtual desktops using hand gestures.
- **Window management**: Snap windows to corners or resize them with gestures.
- **Scrolling gestures**: Scroll up/down by swiping your hand vertically.
- **Mouse control**: Move your cursor with your hand, click with a fist gesture.
- **Zoom in/out**: Pinch your fingers together to zoom in and spread them apart to zoom out.
- **Custom gesture mappings**: Allow users to map their own gestures to system controls.

---

## Installation and Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/rfarrukh0/HandGestureRecognition.git
cd HandAI
```

### 2. Set up the Virtual Environment

Create and activate a Python virtual environment (recommended):

- On **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

The key dependencies are:
- `opencv-python`: OpenCV for video capture and image processing.
- `mediapipe`: Hand tracking using Google’s MediaPipe framework.
- `pycaw`: Python Core Audio Windows Library to control system audio.
- `comtypes`: For interacting with COM objects on Windows.

### 4. Run the Application

To run the application, execute the following command:

```bash
python main.py
```

This will launch the webcam and start the hand gesture recognition system.

---

## How It Works

### Current Functionality

- **Gesture Detection**: The system currently detects an "open palm" gesture by tracking the positions of the thumb and index finger using MediaPipe’s hand tracking solution.
- **System Volume Control**: If the system detects an "open palm," the volume is increased by 10%. This is achieved using the `pycaw` library, which interacts with the Windows audio system.
- **Live Feedback**: 
  - The current FPS (Frames Per Second) is displayed on the top-left of the screen.
  - The detected gesture is displayed right below the FPS in real-time.

### How to Use

1. Run the application as described above.
2. Position your hand in front of the webcam.
3. The system will recognize your "open palm" gesture and increase the system volume.
4. Press 'q' to exit the application.

---

## Future Enhancements

This project is still in the development phase, and many features are planned for future updates:

### 1. **Playback Control**:
   - Use a swipe gesture to skip to the next track or go back to the previous track.
   - Control play/pause with a simple hand gesture.

### 2. **Quick Workspace Switching**:
   - Instantly switch between different virtual desktops by swiping left or right.
   - Use custom hand gestures to move windows between desktops.

### 3. **Window Management**:
   - Snap windows to the left or right half of the screen with swiping gestures.
   - Resize windows by pinching or expanding your fingers.

### 4. **Gesture-Based Scrolling**:
   - Scroll through web pages or documents by swiping your hand up or down.

### 5. **Mouse Control**:
   - Use your hand to control the mouse cursor.
   - Make a fist to simulate a left mouse click.

### 6. **Zoom In/Out**:
   - Implement pinch gestures for zooming in and out on applications, such as maps or image viewers.

### 7. **Custom Gestures**:
   - In the future, users will be able to define their own custom gestures and map them to specific system commands.

---

