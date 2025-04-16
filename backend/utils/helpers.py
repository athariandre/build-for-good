def log_message(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")

def format_emotion_scores(scores):
    return {emotion: round(score, 2) for emotion, score in scores.items()}

def calculate_max_emotion(emotion_counts):
    return max(emotion_counts, key=emotion_counts.get)

def display_error_message(error):
    print(f"Error: {error}")