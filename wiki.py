# importing the module
import wikipedia
import pyttsx3
# finding result for the search
# sentences = 2 refers to numbers of line

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def wikip(com):
    com = com.replace("find", "")
    com = com.replace("information", "")
    com = com.replace("about", "")
    com = com.replace("some", "")
    com = com.replace("collect", "")
    result = str(wikipedia.summary(com, sentences=2))
    SpeakText(result)
    # printing the result
    print(result)