# HandTrackingModule

A lightweight Python helper module for real-time hand tracking, built on top of [OpenCV](https://opencv.org/) and [MediaPipe](https://google.github.io/mediapipe/).

It detects hands in a video stream (e.g. a webcam feed), draws the landmarks, and returns their pixel coordinates so you can build gesture-based or interactive applications on top of it.

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/MohamedAminefattoumi/HandTrackingModule.git
```

Or pin a specific version:

```bash
pip install git+https://github.com/MohamedAminefattoumi/HandTrackingModule.git@v0.1.0
```

## Usage

```python
import cv2
from handtrackingmodule import handDetector

cap = cv2.VideoCapture(0)
detector = handDetector()

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        print(lmList[4])  # thumb tip landmark

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
```

A full working example is available in [`examples/demo.py`](examples/demo.py), including FPS display.

## API

### `handDetector(mode=False, maxHands=2, detection=0.5, trackCon=0.5)`

| Parameter | Description |
|---|---|
| `mode` | `False` for video stream tracking, `True` for static images |
| `maxHands` | Maximum number of hands to detect |
| `detection` | Minimum detection confidence (0–1) |
| `trackCon` | Minimum tracking confidence (0–1) |

### `findHands(img, draw=True)`
Detects hands in the given frame and optionally draws the landmarks and connections. Returns the (possibly annotated) image.

### `findPosition(img, handNo=0, draw=True)`
Returns a list of `[id, x, y]` landmark positions for the given hand index. Returns an empty list if no hand is detected.

## Requirements

- Python >= 3.9
- opencv-python
- mediapipe

## License

No license specified yet.
