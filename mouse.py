

#============================================================================================================================================================

# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
from greeting import greetme
from pynput.mouse import Button, Controller

mouse = Controller()

#for greeting
greetme()

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


#for mode initialization
SpeakText("You have two modes of access one is text input method and second one is voice command please select one to continue.")
mode = int(input("Text input - 1 \nVoice command - 2 \nEnter mode you want to use:"))

# Loop infinitely for user to
# speak
if(mode == 1):
    SpeakText("Text mode is initialized.")
    while (1):
        # Exception handling to handle
        # exceptions at the runtime
        try:
            MyText = input("Enter command : ")
            MyText = MyText.lower()

            if "sleep" in MyText:
                SpeakText("Ok sir, you can call me at any time")
                break
            elif "hello" in MyText:
                SpeakText("Hello sir, how are you ?")
            elif "click" in MyText:
                mouse.click(Button.left, 1)
            elif "right click" in MyText:
                mouse.click(Button.right, 1)
            elif "scroll" in MyText:
                mouse.scroll(0, 2)
            elif "fine" in MyText:
                SpeakText("that's great sir")
            elif "thank you" in MyText:
                SpeakText("You are welcome sir")
            elif "google" in MyText:
                from searching import find
                find(MyText)
                SpeakText("I got this result from Google sir")
            elif "search" in MyText:
                from searching import find
                find(MyText)
                SpeakText("I got this result from Google sir")
            elif "find some information" in MyText:
                from wiki import wikip
                wikip(MyText)
                SpeakText("I got this result from Google sir")
            elif "open" in MyText:
                from app import appop
                appop()
            elif "add" in MyText:
                from rec import adduser
                adduser()
                SpeakText("your face is successfully added in my known list sir")
            elif "identify" in MyText:
                from new import identify
                identify()
            elif "play" in MyText:
                from searching import youtube
                youtube(MyText)
                SpeakText("Ok, let's I play it on youtube sir")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
else:
    SpeakText("Command mode is initialized.")
    # Exception handling to handle
    # exceptions at the runtime
    while (1):
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Your command : ",MyText)

                if "sleep" in MyText:
                    SpeakText("Ok sir, you can call me at any time")
                    break
                elif "hello" in MyText:
                    SpeakText("Hello sir, how are you ?")
                elif "right click" in MyText:
                    mouse.click(Button.right, 1)
                elif "click" in MyText:
                    mouse.click(Button.left, 1)
                elif "down" in MyText:
                    mouse.scroll(0, 3)
                elif "up" in MyText:
                    mouse.scroll(0, -3)
                elif "fine" in MyText:
                    SpeakText("that's great sir")
                elif "thank you" in MyText:
                    SpeakText("You are welcome sir")
                elif "google" in MyText:
                    from searching import find
                    find(MyText)
                    SpeakText("I got this result from Google sir")
                elif "search" in MyText:
                    from searching import find
                    find(MyText)
                    SpeakText("I got this result from Google sir")
                elif "find some information" in MyText:
                    from wiki import wikip
                    wikip(MyText)
                    SpeakText("I got this result from Google sir")
                elif "open" in MyText:
                    from app import appop
                    appop()
                elif "add" in MyText:
                    from rec import adduser
                    adduser()
                    SpeakText("your face is successfully added in my known list sir")
                elif "identify" in MyText:
                    from new import identify
                    identify()
                elif "play" in MyText:
                    from searching import youtube
                    youtube(MyText)
                    SpeakText("Ok, let's I play it on youtube sir")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
