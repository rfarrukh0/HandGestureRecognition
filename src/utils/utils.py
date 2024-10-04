import mediapipe as mp

mp_draw = mp.solutions.drawing_utils

def draw_landmarks(frame, hand_landmarks):
    # draw landmarks and connections on the frame
    mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
