import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake" in query:
            from greeting import greetme
            greetme()

            while True:
                query = takecommand().lower()
                if "sleep" in query:
                    speak("Ok sir, you can call me at any time")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")
                elif "google" in query:
                    from searching import find
                    find(query)
                elif "play" or "song" or "video" in query:
                    from searching import youtube
                    youtube(query)
                elif "temperature" in query:
                    serch = "temprature in tamilnadu"

                    import win32api
                    from win32con import *

                    # Scroll one up
                    win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, 1, 0)

                    # Scroll one down
                    win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)

                    # Scroll one to the right
                    win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, 1, 0)

                    # Scroll one to the left
                    win32api.mouse_event(MOUSEEVENTF_HWHEEL, x, y, -1, 0)

