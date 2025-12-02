import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess

# Logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"


os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level = logging.INFO

)




# Activating voice from our system 
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


# This is speack Function

def speak(text):
    """This function converts text to voice

    Args:
        text
    returns:
        voice
    """

    engine.say(text)
    engine.runAndWait()


speak("Hello my name is Arha")


# This function recognize the speech and convert it to text 

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
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
        logging.info(e)
        print("Say that again please")
        return "None"
    
    return query



def greeting():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir! How are you doing?")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir! How are you doing?")
    else:
        speak("Good Evening Sir! How are you doing?")


speak("I am Arha. Please tell me how may I help you today?")



greeting()

while True:
    query = takeCommand().lower()
    print(query)
    

    if "your name" in query:
        speak("My name is Arha")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime()
        speak(f"Sir the time is {strTime}")

     # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")

    elif "who made you" in query:
        speak("I was created by Bappy sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")

    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")
    

    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")

    
    # Calculator
    elif "open calculator" in query or "calculator" in query:
        speak("Opening calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open Calculator.")

    
     # Notepad
    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad.")

    
    # Command Prompt
    elif "open terminal" in query or "open cmd" in query:
        speak("Opening Command Prompt terminal")
        subprocess.Popen("cmd.exe")
        logging.info("User requested to open Command Prompt.")

    
    # Calendar
    elif "open calendar" in query or "calendar" in query:
        speak("Opening Windows Calendar")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested to open Calendar.")

    
    # YouTube search
    elif "youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        logging.info("User requested to search on YouTube.")

    
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")
        logging.info("User requested to open Facebook.")

    
    elif "open github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")

    # Jokes
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")

    
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")

    
    elif "play music" in query or "music" in query:
        play_music()



    elif "exit" in query:
        speak("Thanks you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

    else: 
        speak("I am sory, I can't help you with that.")
        logging.info("User asked for an unsupported command.")



