import mediapipe as mp
import cv2
import time


BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

def on_result(result, output_image: mp.Image, timestamp_ms: int):
    print(f"Gestures at {timestamp_ms} ms: {result.gestures}")

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path="gesture_recognizer.task"),
    running_mode=VisionRunningMode.LIVE_STREAM,
    num_hands=2,
    result_callback=on_result,
)

with GestureRecognizer.create_from_options(options) as recognizer:

    # Setup webcam
    cap = cv2.VideoCapture(0)
    print("Webcam started! Press q to exit.")
    start_time = time.time()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue
        
        # Flip horizontally for selfie-view & convert BGR to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Calculating timestamp
        timestamp_ms = int((time.time() - start_time) * 1000)

        # Async: automatically drops incoming camera frames when busy so results stay current
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        recognizer.recognize_async(mp_image, timestamp_ms)

        #Display window
        cv2.putText(frame, "Hello World", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv2.imshow("Gesture recognizer", frame)

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows()