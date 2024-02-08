import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
print ("intializing jarvis")
MASTER = "Sir"
engine = pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#speak function to pronounce string 
def speak(text):
    engine.say(text)
    engine.runAndWait()
#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("hello good Morning"+ MASTER)

    elif hour>=12 and hour <18:
        speak("hello good afternoon"+ MASTER)

    else:
        speak("hello good evening"+ MASTER)    

    speak("I am jarvis. I am always at your service. What you want me to do?")

#this function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception:
        print("say that again please")
        query = None
    
    return query


#def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('nitinrajput6387417@gmail.com','password')
    #server.sendmail("nitinrajput6387417@gmail.com", to, content)
    #server.close()
def main():
    #main program starts
    speak("intializing jarvis...")
    wishMe()
    query = takeCommand()

    #logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)


    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'c:/program Files (x86)/Google/chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = 'c:/program Files (x86)/Google/chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
        url = "reddit.com"
        chrome_path = 'c:/program Files (x86)/Google/chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif 'play music' in query.lower():
        songs_dir = "c:\\Users\\Nitin\\Downloads\\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Nitin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)

main()
