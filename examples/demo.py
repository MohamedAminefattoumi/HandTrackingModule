
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Importing libraries
from handtrackingmodule.detector import handDetector
import cv2
import mediapipe as mp
import time


def main():
    # Start capturing video from the default webcam (index 0)
    cap = cv2.VideoCapture(0)

    # Variables used to calculate frames per second (FPS)
    pTime = 0
    cTime = 0

    # Create an instance of the hand detector
    detector = handDetector()

    while True:
        # Read a frame from the webcam
        success, img = cap.read()
        if not success:
            print("Failure occurred while accessing the camera")
            break

        # Detect hands and draw landmarks on the frame
        img = detector.findHands(img=img)
        # Get the list of landmark positions for the first detected hand
        lmList = detector.findPosition(img)

        # If a hand was detected, print the position of landmark id 4 (thumb tip)
        if len(lmList) != 0:
            print(lmList[4])

        # Calculate FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS on the frame
        cv2.putText(img, str(int(fps)), (10, 78), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        # Show the resulting frame in a window
        cv2.imshow("Image", img)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()