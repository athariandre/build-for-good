import numpy as np

class Student:
    def __init__(self, neutral, sadness, surprise, happiness, anger, fear):
        self.neutral = neutral
        self.sadness = sadness
        self.surprise = surprise
        self.happiness = happiness
        self.anger = anger
        self.fear = fear

    class Student:
        """
            WEIGHTS: A dictionary containing predefined weights for different emotion types.
                These weights are used to calculate scores for specific emotions based on the 
                student's emotional state. Each key in the dictionary corresponds to an emotion 
                type (e.g., "boredom", "attentiveness", "confusion"), and the value is a list of 
                weights associated with the respective emotion components.
        """
        
        WEIGHTS = {
            "boredom": [0.035, 1.24e-06, 0.00113, 0.941, 3.88e-05, 1.28e-05],
            "attentiveness": [0.79, 0.000638, 0.000275, 0.000638, 0.184, 0.002],
            "confusion": [0.042, 0.042, 0.019, 0.001, 0.002, 0.898],
        }

        def calculate_score(self, emotion_type):
            if emotion_type not in self.WEIGHTS:
                raise ValueError(f"Unknown emotion type: {emotion_type}")
            weights = np.array(self.WEIGHTS[emotion_type])
            emotions = np.array([self.neutral, self.sadness, self.surprise, self.happiness, self.anger, self.fear])
            return np.dot(weights, emotions)

        def __init__(self, neutral, sadness, surprise, happiness, anger, fear):
            self.neutral = neutral
            self.sadness = sadness
            self.surprise = surprise
            self.happiness = happiness
            self.anger = anger
            self.fear = fear
            self.boredom = self.calculate_score("boredom")
            self.attentiveness = self.calculate_score("attentiveness")
            self.confusion = self.calculate_score("confusion")

    def print_scores(self):
        print("Emotion Scores:")
        print(f"Neutral: {self.neutral}")
        print(f"Sadness: {self.sadness}")
        print(f"Surprise: {self.surprise}")
        print(f"Happiness: {self.happiness}")
        print(f"Anger: {self.anger}")
        print(f"Fear: {self.fear}")