from emotions.student import Student
from deepface import DeepFace


def analyze_image(i):
    path = f"/Users/andre/Projects/competition/build-for-good/images/frame-{i}.jpg"
    # path = "test.jpg" # for testing
    return DeepFace.analyze(
        img_path = path, actions = ['emotion']
    )

def analyze_emotions(out_dict):
    student_dict = []
    for person in out_dict:
        print(out_dict)
        student_dict.append(
            Student(
                person['emotion']['neutral'],
                person['emotion']['sad'],
                person['emotion']['surprise'],
                person['emotion']['happy'],
                person['emotion']['angry'],
                person['emotion']['fear']
            )
        )
    
    return student_dict

def calculate_emotional_counts(student_dict):
    attentive_count = 0
    bored_count = 0
    confused_count = 0
    
    for student in student_dict:
        boredom = student.boredom
        attentiveness = student.attentiveness
        confusion = student.confusion
        
        maxemotion = max([boredom, attentiveness, confusion])
        
        if maxemotion == boredom:
            bored_count += 1
        elif maxemotion == attentiveness:
            attentive_count += 1
        else:
            confused_count += 1
            
    return attentive_count, bored_count, confused_count

def display_emotional_message(attentive_count, bored_count, confused_count, disp):
    if bored_count >= attentive_count and bored_count >= confused_count:
        disp.display_message(speedUp=True)
    elif confused_count >= attentive_count and confused_count >= bored_count:
        disp.display_message(slowDown=True)
    else:
        disp.display_message()