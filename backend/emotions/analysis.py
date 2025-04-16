def analyze_emotions(out_dict):
    student_dict = []
    
    for person in out_dict:
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
        boredom = student.calculate_boredom()
        attentiveness = student.calculate_attentiveness()
        confusion = student.calculate_confusion()
        
        maxemotion = max([boredom, attentiveness, confusion])
        
        if maxemotion == boredom:
            bored_count += 1
        if maxemotion == attentiveness:
            attentive_count += 1
        if maxemotion == confusion:
            confused_count += 1
            
    return attentive_count, bored_count, confused_count

def display_emotional_message(attentive_count, bored_count, confused_count, display_message_func):
    if bored_count >= attentive_count and bored_count >= confused_count:
        display_message_func(speedUp=True)
    elif confused_count >= attentive_count and confused_count >= bored_count:
        display_message_func(slowDown=True)
    else:
        display_message_func()