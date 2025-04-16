import cv2
import time

def start_camera():

    cap = cv2.VideoCapture(0)
    time.sleep(1)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    return cap

def capture_frame(cap, frame_index):
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'images/frame-{frame_index}.jpg', frame)
        return ret, frame
    return None

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()