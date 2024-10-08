import cv2

def initialize_camera(camera_index=0):
    # initialize camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise Exception("could not open video device")
    return cap

def capture_frame(cap):
    # capture frame from webcam
    ret, frame = cap.read()
    if not ret:
        raise Exception("failed to capture frame")
    return frame
