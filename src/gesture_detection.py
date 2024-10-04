import mediapipe as mp
import cv2

def initialize_hands():
    # initialize mediapipe hand detection
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.95, min_tracking_confidence=0.95)
    return hands

def detect_gesture(frame, hands):
    # convert frame to rgb and detect hand landmarks
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_tip_x = hand_landmarks.landmark[4].x
            index_finger_tip_x = hand_landmarks.landmark[8].x

            # check if thumb is to the left of the index finger (open palm gesture)
            if thumb_tip_x < index_finger_tip_x:
                return "open palm", hand_landmarks
    return None, None
