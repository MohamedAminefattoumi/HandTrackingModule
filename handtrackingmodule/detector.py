# Importing libraries
import cv2
import mediapipe as mp
import time


class handDetector():
    """
    A hand detector class built on top of the MediaPipe Hands solution.
    Detects hand landmarks in a video frame and allows retrieving
    their pixel coordinates.
    """

    def __init__(self, mode=False, maxHands=2, detection=0.5, trackCon=0.5):
        # Whether to treat input images as a batch of static images (True)
        # or as a continuous video stream (False, enables tracking)
        self.mode = mode
        # Maximum number of hands to detect
        self.maxHands = maxHands
        # Minimum confidence value for hand detection to be considered successful
        self.detection = detection
        # Minimum confidence value for the landmark tracking to be considered successful
        self.trackCon = trackCon

        # Initialize the MediaPipe Hands solution
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        # Utility to draw the hand landmarks and connections on the image
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """
        Detects hands in the given image and optionally draws
        the landmarks and connections on it.
        """
        # MediaPipe expects RGB images, but OpenCV reads images in BGR by default
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the image to detect hand landmarks
        self.results = self.hands.process(imgRGB)

        # If at least one hand was detected
        if self.results.multi_hand_landmarks:
            # Loop through each detected hand
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    # Draw the landmarks and their connections on the original image
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        """
        Returns a list of landmark positions (id, x, y) for a given hand.
        By default, returns the positions for the first detected hand (handNo=0).
        """
        lmList = []

        if self.results.multi_hand_landmarks:
            # Select the requested hand (by index) from the list of detected hands
            myHand = self.results.multi_hand_landmarks[handNo]

            # Loop through each landmark (21 points per hand)
            for id, lm in enumerate(myHand.landmark):

                # Get image dimensions to convert normalized coordinates to pixel coordinates
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

                if draw:
                    # Draw a filled circle on each landmark point
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return lmList


