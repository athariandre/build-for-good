def start_camera():
    import cv2
    import time

    cap = cv2.VideoCapture(0)
    time.sleep(1)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    return cap

def capture_frame(cap, frame_index):
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'frame-{frame_index}.jpg', frame)
        return frame
    return None

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()