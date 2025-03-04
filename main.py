import pyttsx3  # pip install pyttsx3
import datetime  # module
from AppOpener import open, close
import speech_recognition as sr
import wikipedia
import smtplib
import pywhatkit
import webbrowser as wb
import os  # inbuilt
import pyautogui
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import requests, json  # inbuilt

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Please login into your account.")
logid = input("Enter your login ID: ")
logpass = input("Enter your password : ")
speak("Login successful")


# for mode initialization
speak("Hi, You have two modes of access.First one is text input method and second one is voice command please select one to continue.")
mode = int(input("Text input - 1 \nVoice command - 2 \nEnter mode you want to use:"))

if mode == 1:
    speak("Text mode is initialized. you can enter your input on my screen")
else:
    speak("Command mode is initialized. You can command me by your voice")

speak("Wait a second I will initialize and test my command finctions.")
for i in range(10):
    print("Loading functions...")
speak("Tank you for waiting, Initialization and testing got done.")

# change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


# time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


# date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")


# welcome function
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Sam at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning... Have a nice day")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon... Have a nice day")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening... Have a nice day")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


# command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # speak(query)
        # print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


# sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("2k20it29@kiot.ac.in", "SJ000$sj000")
    server.sendmail("2k20it29@kiot.ac.in", to, content)
    server.close()


# screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "screenshot/1.png"
    )


# battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


# joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)


# weather condition
def weather():
    api_key = "YOUR-API_KEY"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    if mode == 2:
        city_name = takeCommand()
    else:
        city_name = input()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
                                                       " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    speak(
        "I am Sam, version 1.6, I am a multipurpose AI, I am developed by Sanjai on feb 15th 2023 in INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        if mode == 2:
            query = takeCommand().lower()
        else:
            query = input("Your command : ").lower()
        # time

        if ('time' in query):
            time()

        # date

        elif ('date' in query):
            date()

        # personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

        # searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

        # sending email

        elif ("send email" in query or "mail" in query):
            try:
                speak("What is the message for the email")
                if mode == 2:
                    content = takeCommand()
                else:
                    content = input()

                speak("Please Enter the mail id here to send mail to the correct destination")
                to = input()
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient")
        elif ("google" in query or "search" in query):

            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

            #wb.get(chromepath).open_new_tab(search + '.com')
            query = query.replace("google", "")
            query = query.replace("search", "")
            query = query.replace("about", "")
            query = query.replace("some information", "")
            pywhatkit.search(query)
            speak("I found this result from google")

        # sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

        # play songs

        elif ("play songs" in query or "play" in query):

            query = query.replace("find on", "")
            query = query.replace("find", "")
            query = query.replace("about", "")
            query = query.replace("youtube", "")
            query = query.replace("play", "")
            query = query.replace("play on", "")
            pywhatkit.playonyt(query)
            speak("I play this video from Youtube")

        # reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            if mode == 2:
                data = takeCommand()
            else:
                data = input()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        # reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        # screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

        # cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

        # jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

        # weather
        elif ("weather" in query or "temperature" in query):
            weather()

        # jarvis features
        elif ("tell me your powers" in query or "help" in query
              or "features" in query or "what can you" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            i can add you as an person in my known list then i can identify you at anywhere
            i can learn the information from the internet
            And yes one more thing, My boss is working on this system to add more features...,
            That's all about me.
            '''
            print(features)
            speak(features)

        elif ("hi" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("sam", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

        # changing voice
        elif ("voice" in query):
            print("for female say female and, for male say male")
            speak("for female, say female and for male, say male")
            if mode == 2:
                q = takeCommand()
            else:
                q = input()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

        elif ("add user" in query):
            from rec import adduser
            from new import identify
            speak("Please enter your name sir")
            if mode == 2:
                com = takeCommand()
            else:
                com = input("Enter your name : ")
            adduser(com)
            speak("Process completed. Now I can Identify you.")
            identify()


        elif ("learn" in query or "learning" in query):
            from learn import lrn
            speak("Enter the Object I want to learn")
            lrn()
            speak("Done, I have learned the object you said")

        elif ("test" in query or "check" in query):
            from check import deliv
            deliv()

        elif ("open" in query):
            app_name = query.replace("open ", "")
            open(app_name, match_closest=True)

        elif ("close" in query):
            app_name = query.replace("close ", "").strip()
            close(app_name, match_closest=True, output=False)


            # exit function

        elif ('i am done' in query or 'bye bye sam' in query
              or 'go offline sam' in query or 'bye' in query
              or 'nothing' in query or "sleep" in query):
            wishme_end()






































