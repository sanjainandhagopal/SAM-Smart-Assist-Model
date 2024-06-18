# import the modules
import os
from PIL import Image
from os import listdir
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def deliv():
    # to list the contents
    cont = "objects"
    speak("I have learned about the topics such as")
    i = 1
    for tp in os.listdir(cont):
        speak(tp)
        print(i, ".", tp)
        i += 1
    # get the path or directory
    speak("Enter the topic then I will explain")
    inp = input("Enter the topic to explain : ")
    folder_dir = "objects/"
    folder_dir += inp
    for images in os.listdir(folder_dir):

        # check if the image ends with png or jpg or jpeg
        if (images.endswith(".png") or images.endswith(".jpg") \
                or images.endswith(".jpeg")):
            dir = folder_dir
            dir += "/"
            dir += images
            im = Image.open(dir)
            im.show()
            dir = "objects/"
            dir += inp
            dir += "/data.txt"
            reminder_file = open(dir, 'r')
            speak("You said me to remember that: " + reminder_file.read())
            break

