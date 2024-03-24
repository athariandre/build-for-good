# Lecture Assistant

__Note:__ the code has been fully condensed into the backend/webcam.py file for now, it's getting fixed soon, still works as intended. also, in order to run the facial recognition model, clone the repository at github.com/serengil/deepface and run the api.py file in /deepface/api/src

Howdy! This is my groups submission for the TACS “build for good” hackathon. 

We created Lecture Assistant. A tool powered by AI to assist teachers in maintaining a lecture speed that accomodates the class’ needs. Lecture Assistant takes a live video feed, from a camera set up by the professor, and indicates to the teacher whether they are lecturing too fast, too slow, or just right.

By using the deep face neural network, our program can predict the emotions of any students captured in the camera, and calculates if too many students are either confused, attentive, or bored, and alerts the teacher so that they can change their teaching speed.

We created Lecture Assistant because we found it very frustrating that our professors would either teach too slow or too fast. Whether it be through struggling to write down an entire slide in 20 seconds, or fighting the urge to fall asleep as the professor rambles on, the issue of instruction being based on the teachers desired speed rather than the student’s learning speed is something that we (and hopefully other students as well) have to deal with daily.

We used a facial recognition software named deepface, and ran in on a local network so that our program could could interact with it. Then, using a python library called cv2, we fed live webcam data to the model and recieved emotion scores. The issue, however, with the facial recognition model we used, was that the model was only capable of predicting emotions such as happy, sad, angry, surprised, and fearful, and wasnt able to detect whether someone was bored, attentive, or confused.

To tackle this, we analyzed multiple different images of people being confused, attentive, and bored, and figure out what combination of emotions were tied most closely to boredom, attentiveness, and confusion. After a few hours of analysis, we finally narrowed down the weights we needed to give to each emotion to accurately detect whether a student was bored, attentive, or confused.

Once we could detect a student’s emotion to better suit our needs, we then found the ratio of students who were struggling with the instructional speed, and determined if the teacher should speed up, slow down, or maintain their pace when teaching.

In order to keep things simple for the teacher, we decided the front end should only incorporate one thing; how the teacher should continue instructing. We created a simple window using PyQt5 which would display what the teacher should do regarding instruction.

And that’s it! A simple, yet effective tool that can hopefully be used by professors anywhere.  
