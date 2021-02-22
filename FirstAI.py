import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


while True:
    with speech_recognition.Microphone() as mic: 
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    try: 
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    if "hello" in you: 
        robot_brain = "hello Minh"
    elif "morning" in you:
        robot_brain = "good morning! Minh"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "" in you:
        robot_brain = "I dont understand" 
    elif "bye" in you:
        robot_brain = "Bye Minh DDS"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Sorry, I dont understand!"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

# nhan dạng giọng nói -> AI dummy -> speakspeak