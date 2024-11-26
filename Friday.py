import pyttsx3      # Python's "Text to Speech" module
import datetime     # Builtin module to get the DateTime
import speech_recognition as sr  # For speech recognition from the microphone
import wikipedia    # For searching and summarizing Wikipedia articles
import webbrowser   # To open websites in a browser
import pywhatkit    # For tasks like playing YouTube videos or sending WhatsApp messages
import smtplib      # For sending emails
import os           # For interacting with the operating system
import pyjokes      # To fetch jokes

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')  # 'sapi5' is a speech API provided by Microsoft
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice to the first one in the system

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Friday, my owner is Mr. Subham. Please tell me how may I help you")

# Function to take voice input from the user and return it as text
def takecommand():
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the microphone as the input source
        print("Listening...")
        r.pause_threshold = 1  # Wait for 1 second of silence before processing
        audio = r.listen(source)  # Capture the audio

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google API
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"  # Return "None" if recognition fails
    return query

# Function to send an email using SMTP
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server
    server.ehlo()  # Identify with the mail server
    server.starttls()  # Start TLS encryption
    server.login('subhampal7063@gmail.com', 'SUBHAMpal')  # Login credentials
    server.sendmail('subhampal7063@gmail.com', to, content)  # Send the email
    server.close()  # Close the server connection

# Main function to handle user queries
if __name__ == "__main__":
    wishme()  # Greet the user
    while True:
        query = takecommand().lower()  # Convert the query to lowercase

        # Handle Wikipedia queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # Fetch 2 sentences from Wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open specific websites
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

        # Play a song or video on YouTube
        elif 'play' in query:
            song = query.replace('play', '')
            speak('Playing ' + song)
            print('Playing ' + song)
            pywhatkit.playonyt(song)

        # Tell a joke
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # Tell the current time
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        # Send an email
        elif 'email to me' in query:
            try:
                speak('What should I write?')
                content = takecommand()  # Take the email content
                to = "subhampal7063@gmail.com"  # Recipient's email
                sendemail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry boss! I am not able to send this email at the moment because of a network issue")

        # Open Visual Studio Code
        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        # Respond to casual conversation
        elif 'how are you' in query:
            speak("I am fine, I hope you are fine too")
        elif 'love' in query:
            speak("Thanks for loving me, I also love myself so much")

        # Placeholder for news (to be implemented)
        elif 'news' in query:
            speak("Sorry Sir, this function is not implemented till now")

