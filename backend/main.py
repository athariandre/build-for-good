import cv2
import time 
import sys
from deepface import DeepFace
from PyQt5.QtWidgets import QApplication
from ui.display import display_message
from emotions.student import Student
from camera.capture import start_camera, capture_frame
from emotions.analysis import analyze_emotions

app = QApplication(sys.argv)

cap = start_camera()
i = 0

if not cap:
    print("Error: Could not access the camera.")
    sys.exit(1)

while True: 
    ret, frame = capture_frame(cap, i)

    if ret: 
        out_dict = analyze_emotions(frame)

        student_dict = []

        try:
            for person in out_dict:
                student_dict.append(
                    Student(
                        person['emotion']['neutral'],
                        person['emotion']['sad'],
                        person['emotion']['surprise'],
                        person['emotion']['happy'],
                        person['emotion']['angry'],
                        person['emotion']['fear']
                    ))
                
            attentive_count, bored_count, confused_count = 0, 0, 0
            for student in student_dict:
                boredom = student.boredom
                attentiveness = student.attentiveness
                confusion = student.confusion
                maxemotion = max([boredom, attentiveness, confusion])
                if maxemotion == boredom:
                    bored_count += 1
                if maxemotion == attentiveness:
                    attentive_count += 1
                if maxemotion == confusion:
                    confused_count += 1

            print(f"attentive: {attentive_count}\nbored: {bored_count}\nconfused: {confused_count}")

            if bored_count >= max(attentive_count, confused_count):
                display_message(speedUp=True)
            elif confused_count >= max(attentive_count, bored_count):
                display_message(slowDown=True)
            else:
                display_message()

        except Exception as e:
            print("people not found!")
            print(f"\n\n\n ERROR: {e} \n\n\n")
            pass
        
        i += 5
        time.sleep(5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
    else:  
        break 

cap.release() 
cv2.destroyAllWindows()