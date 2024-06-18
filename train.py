# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
from greeting import greetme

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


# Loop infinitely for user to
# speak
def star():
    while (1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.1)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                if "sleep" in MyText:
                    SpeakText("Ok sir, you can call me at any time")
                    break
                elif "hello" in MyText:
                    SpeakText("Hello sir, how are you ?")
                elif "fine" in MyText:
                    SpeakText("that's great sir")
                elif "thank you" in MyText:
                    SpeakText("You are welcome sir")
                elif "google" in MyText:
                    from searching import find
                    find(MyText)
                    SpeakText("I got this result from Google sir")
                elif "add" in MyText:
                    from rec import adduser
                    adduser()
                    SpeakText("your face is successfully added in my known list sir")
                elif "identify" in MyText:
                    from new import identify
                    identify()
                elif "play" or "song" or "video" in MyText:
                    from searching import youtube
                    youtube(MyText)
                    SpeakText("Ok, let's I play it on youtube sir")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
