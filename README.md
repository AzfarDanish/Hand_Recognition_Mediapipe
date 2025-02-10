# Hand Recognition with MediaPipe

A real-time hand tracking and recognition system using OpenCV and MediaPipe. This project detects hands, tracks their landmarks, and counts extended fingers.

## Features

- **Hand Detection**: Uses Google's MediaPipe to track hands in real time.
- **Finger Counting**: Identifies which fingers are extended.
- **Bounding Box & Labels**: Draws a bounding box around the detected hand, displays finger count, and identifies left/right hand.
- **Real-Time Performance**: Optimized for smooth frame processing.

## Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/AzfarDanish/Hand_Recognition_Mediapipe.git
   cd Hand_Recognition_Mediapipe
   ```

2. **Set up a virtual environment (Recommended)**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Upgrade pip and install dependencies**

   ```sh
   pip install --upgrade pip setuptools wheel
   pip install opencv-python opencv-contrib-python mediapipe
   ```

## Usage

Run the following command to start hand recognition:

```sh
python main.py
```

### Controls:

- Press `q` to exit the application.

## File Overview

| File               | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `main.py`          | Main script to capture video, process frames, and display results. |
| `hand_tracking.py` | Handles hand detection and landmark processing using MediaPipe.    |
| `bounding_box.py`  | Draws bounding boxes and labels around detected hands.             |

## How It Works

1. **Frame Processing**

   - Captures video from webcam.
   - Flips the frame for a mirrored view.

2. **Hand Detection**

   - MediaPipe identifies hand landmarks.
   - Determines if fingers are extended.

3. **Drawing and Display**

   - Bounding boxes are drawn.
   - FPS is displayed on the top-left.

## Future Improvements

- Add gesture recognition.
- Improve finger counting stability.
- Support multiple hands with different gestures.

## License

This project is licensed under the MIT License.

