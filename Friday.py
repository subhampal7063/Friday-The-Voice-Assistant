import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("Good AFTERNOON")

    else :
        speak("Good Evening")

    speak("I am friday, MY onwer is Mr. SUBHAM, Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("say that again...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('subhampal7063@gmail.com', 'SUBHAMpal')
    server.sendmail('subhampal7063@gmail.com', to, content)
    server.close()




if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gfg' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open hackerrank' in query:
            webbrowser.open("https://www.hackerrank.com/products/main/")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play' in query:
            song = query.replace('play','')
            speak('playing'+ song)
            print('playing'+ song)
            pywhatkit.playonyt(song)
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")
        elif 'email to me' in query:
            try:
                speak('what should i write')
                content = takecommand()
                to = "subhampal7063@gmail.com"
                sendemail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry boss! I am not able to send this email at the moment because of network issue")
        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        elif 'how are you' in query:
            speak("I am fine, I hope you are fine too")
        elif 'love' in query:
            speak("Thanks for loving me, I also love me so much")
        elif 'news' in query:
            speak("sir, kindly tell me,  what type of news you want ")
        elif 'who is your owner' in query:
            speak("I am a AI, I am created by Subham")