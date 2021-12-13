import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak("I'm Friday, How may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio, language="en-in")
        print("User said: ", query)
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia", "")
            try:
                results=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia...")
                print(results)
                speak(results)
            except Exception:
                print("Having some issues with wikipedia, Come again?")
                speak("Having some issues with wikipedia, Come again?")
        elif 'open youtube' in query:
            speak("Opening Youtube......")
            webbrowser.open_new_tab("youtube.com")
        elif 'open google' in query:
            speak("Opening google.......")
            webbrowser.open_new_tab("google.com")
        elif 'open github' in query:
            speak("Opening Github.....")
            webbrowser.open_new_tab("github.com")
        elif 'google' in query:
            speak("Google search is not available, searching wikipedia instead.....")
            query=query.replace("google", "")
            try:
                results=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia...")
                print(results)
                speak(results)
            except Exception:
                print("Having some issues with wikipedia, Come again?")
                speak("Having some issues with wikipedia, Come again?")
        elif 'open spotify' in query:
            speak("opening spotify......")
            webbrowser.open_new_tab("open.spotify.com")
        elif 'open whatsapp' in query:
            speak("Opening whatsapp.....")
            webbrowser.open_new_tab("web.whatsapp.com")
        elif 'open instagram' in query:
            speak("You look amazing boss!!!")
            webbrowser.open_new_tab("https://www.instagram.com/derex_ig/")
        elif 'hi friday' in query:
            speak("Hello Boss!!!")
        elif 'tell me about yourself friday' in query:
            speak("Boss!!!! You made me and now asking for introduction! It's hilarious!!!!")
        elif 'friday will you be my girlfriend' in query:
            speak("Don't expect anything physical from me!")
        elif 'do you like jarvis' in query:
            speak("Not at all!! But I like Mr. Tony!")
        else:
            speak("Come again boss!")