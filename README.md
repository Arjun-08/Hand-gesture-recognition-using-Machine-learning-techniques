## Hand Gesture Recognition Using Machine Learning Techniques

### Overview

This repository contains Python code for recognizing hand gestures using machine learning techniques to control media playback functions. The implementation leverages the MediaPipe framework for hand detection and tracking, and pyautogui and pycaw libraries for controlling keyboard, mouse, and audio functions, respectively.

### Modules

1. **handDetectorModule.py**
   - **Description**: This module processes video input from the system's webcam to detect hands and draw landmarks on them.
   - **Functionality**:
     - Captures webcam video feed.
     - Detects hands in the input images using MediaPipe's hand detection model.
     - Draws landmarks on the detected hands.
     - Creates and returns a list of landmark positions.

2. **gestureMediaControl.py**
   - **Description**: This module interprets hand gestures detected by `handDetectorModule.py` to control media playback.
   - **Functionality**:
     - Imports `pyautogui` for keyboard and mouse controls and `pycaw` for audio controls.
     - Utilizes custom gestures defined using the landmark data from the hand detection module.
     - Implements the following controls:
       - **Volume Control**: Adjusts volume based on the distance between the index finger and thumb.
       - **Play/Pause**: Toggles media playback when the thumb is folded, and all other fingers are folded.
       - **Forward**: Skips forward by five seconds when three fingers are folded, and the little finger is open.
       - **Rewind**: Rewinds by five seconds when three fingers are folded, and the index finger is open.

### Benefits of Hand Gesture Recognition for Media Control

- **Touchless and Hands-Free**: Provides a convenient and user-friendly interface, especially useful when hands are occupied or when there is no direct access to media playback controls.
- **Real-Time Tracking**: Uses advanced image processing and computer vision techniques for real-time hand tracking and gesture recognition.
- **Customizable**: The MediaPipe framework allows for fine-tuning the pre-trained model with custom hand gesture images to recognize specific gestures and map them to desired media control functions.

### Implementation Details

- **MediaPipe Framework**: Utilized for hand detection and tracking. It provides a pre-trained model that can be adapted for custom gesture recognition.
- **pyautogui Library**: Used for simulating keyboard and mouse actions based on recognized gestures.
- **pycaw Library**: Used for controlling system audio based on recognized gestures.

### Getting Started

To get started with hand gesture recognition for media control, follow these steps:

1. **Install Dependencies**: Ensure you have the necessary Python libraries installed:
   ```bash
   pip install numpy pandas mediapipe pyautogui pycaw
   ```

2. **Run the Modules**: Execute the `handDetectorModule.py` to start detecting hand gestures, and then run `gestureMediaControl.py` to control media playback based on detected gestures.

3. **Customization**: Modify the gesture definitions in `gestureMediaControl.py` to suit your specific needs and preferences.

### Conclusion

Hand gesture recognition for media control is an innovative application of machine learning techniques, providing an intuitive and efficient way to interact with media playback functions. By leveraging the MediaPipe framework and integrating it with libraries like pyautogui and pycaw, this project demonstrates the practical utility of real-time hand gesture detection and recognition.

---
## Contact
If you have any questions or suggestions, please feel free to reach out to me at [nvarjunmani07@gmail.com](mailto:nvarjunmani07@gmail.com).
