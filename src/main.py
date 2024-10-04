import time
import cv2
from gesture_detection import detect_gesture, initialize_hands
from camera_utils import initialize_camera, capture_frame
from audio_control import adjust_volume
from utils import draw_landmarks

# initialize camera and mediapipe hands
cap = initialize_camera()
hands = initialize_hands()

# set variables for volume control
last_volume_up_time = 0
volume_up_interval = 1  # 1 second interval between volume increases

# start video capture
prev_time = 0  # used for FPS calculation

while True:
    frame = capture_frame(cap)

    # get current time for FPS calculation
    current_time = time.time()

    # calculate FPS
    fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
    prev_time = current_time

    # detect hand gesture
    gesture, hand_landmarks = detect_gesture(frame, hands)

    # volume control based on gesture
    if gesture == "open palm":
        if current_time - last_volume_up_time > volume_up_interval:
            adjust_volume("up")
            last_volume_up_time = current_time

    # draw landmarks if available
    if hand_landmarks:
        draw_landmarks(frame, hand_landmarks)

    # display the FPS on the frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # display the gesture on the frame
    if gesture:
        cv2.putText(frame, f'Gesture: {gesture}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # show video feed
    cv2.imshow("Hand Gesture Recognition", frame)

    # exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
