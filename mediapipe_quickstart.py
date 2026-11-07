import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 1. Download the hand_landmarker.task model file from MediaPipe's official site and place it in your project folder.
# URL: https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

detector = vision.HandLandmarker.create_from_options(options)

# Open default webcam (0)
cap = cv2.VideoCapture(0)
print("Camera started! Press 'q' to exit window.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # Flip horizontally for selfie-view & convert BGR to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert OpenCV image to MediaPipe Image format
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect hand landmarks synchronously
    results = detector.detect(mp_image)

    # Draw landmarks (custom drawing or using mp solutions if compatible)
    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            # Draw points manually or integrate with drawing utilities if available
            for landmark in hand_landmarks:
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    cv2.imshow('Saturday Hack Night - MediaPipe Quickstart', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()