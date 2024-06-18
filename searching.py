import pywhatkit

def find(query):
    if "google" in query:
        query = query.replace("find","")
        query = query.replace("about","")
        query = query.replace("google","")
        pywhatkit.search(query)

def youtube(query):
    if "play" in query:
        query = query.replace("find on", "")
        query = query.replace("find", "")
        query = query.replace("about", "")
        query = query.replace("youtube", "")
        query = query.replace("play", "")
        query = query.replace("play on", "")
        pywhatkit.playonyt(query)

