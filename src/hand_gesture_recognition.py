import cv2
import mediapipe as mp
import pyautogui
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# initialize mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.95, min_tracking_confidence=0.95)
mp_draw = mp.solutions.drawing_utils

# get webcam video
cap = cv2.VideoCapture(0)

# vol variables
last_volume_up_time = 0
volume_up_interval = 1

# audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# start video capture
while True:
    # read frames
    ret, frame = cap.read()
    if not ret:
        break

        # convert to RGB for mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # check for landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # extract landmarks
            landmarks = hand_landmarks.landmark
            thumb_tip_x = landmarks[4].x
            index_finger_tip_x = landmarks[8].x

            if thumb_tip_x < index_finger_tip_x:
                gesture = "Open Palm"
                print(gesture)  # log

                # display gesture on feed
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # volume control
                current_time = time.time()

                if current_time - last_volume_up_time > volume_up_interval:
                    current_volume = volume.GetMasterVolumeLevelScalar()
                    volume.SetMasterVolumeLevelScalar(min(current_volume + 0.1, 1.0), None)
                    last_volume_up_time = current_time

    # show frames
    cv2.imshow("Hand Gesture Recognition", frame)

    # exit on q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
