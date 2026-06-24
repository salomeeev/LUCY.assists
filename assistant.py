import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def talk(text):
    print("🎙️ LUCY:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)

        try:
            voice = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )
        except sr.WaitTimeoutError:
            return ""

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
        return command

    except sr.UnknownValueError:
        talk("Sorry bro, I didn't catch that.")
        return ""

    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""

def run_lucy():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who are you" in command:
        talk("I am Lucy, your AI voice assistant.")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open chatgpt" in command or "open chat gpt" in command:
        talk("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")
    
    elif "open whatsapp" in command or "whatsapp" in command:
        talk("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    
    elif "who created you" in command or "who made you" in command:
        talk("I was created by Salome, an AI and Data Science student.")

    elif "search" in command:
        query = command.replace("search", "").strip()
        talk(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "introduce yourself" in command:
        talk("Hello. I am Lucy, your personal voice assistant. I can search the web, open applications, play music, and help with daily tasks.")

    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")


talk("Hello. I am Lucy, your personal AI voice assistant. How can I help you today?")
while True:
    run_lucy()