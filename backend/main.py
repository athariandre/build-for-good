import cv2
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from ui.display import Display
from camera.capture import start_camera, capture_frame, release_camera
from emotions.analysis import analyze_image, analyze_emotions, calculate_emotional_counts, display_emotional_message


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.display = Display()
        self.display.show()

        self.cap = start_camera()
        if not self.cap:
            print("Error: Could not access the camera.")
            sys.exit(1)

        self.frame_index = 0

        # Set up a timer to process frames periodically
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)
        self.timer.start(5000)  # Process a frame every 5 seconds

    def process_frame(self):
        ret, frame = capture_frame(self.cap, self.frame_index)
        if not ret:
            self.timer.stop()
            release_camera(self.cap)
            return

        try:
            # Analyze the image and emotions
            out_dict = analyze_image(self.frame_index)
            student_dict = analyze_emotions(out_dict)
            attentive_count, bored_count, confused_count = calculate_emotional_counts(student_dict)

            # Print emotional counts
            print(f"attentive: {attentive_count}\nbored: {bored_count}\nconfused: {confused_count}")

            # Update the display based on the emotional analysis
            display_emotional_message(attentive_count, bored_count, confused_count, self.display)

        except Exception as e:
            print("Error processing frame:", e)

        self.frame_index += 5

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = MainApp()
    app.run()