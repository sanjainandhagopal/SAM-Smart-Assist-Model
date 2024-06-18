from AppOpener import open, close
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def appop():
    SpeakText("Please enter the app name.")
    print("1. Open <any_name> TO OPEN APPLICATIONS")
    print("2. Close <any_name> TO CLOSE APPLICATIONS")
    print()
    open("help")
    print("TRY 'OPEN <any_key>'")

    while True:
        inp = input("ENTER APPLICATION TO OPEN / CLOSE: ").lower()
        if "close " in inp:
            app_name = inp.replace("close ","").strip()
            close(app_name, match_closest=True, output=False)  # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
        if "open " in inp:
            app_name = inp.replace("open ","")
            open(app_name, match_closest=True)  # App will be open be it matches little bit too