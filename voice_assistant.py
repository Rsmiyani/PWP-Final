import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os


listener = sr.Recognizer()
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print(" Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
    except:
        command = ""
    return command

def run_assistant():
    say("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print("🕒", time)
            say('Current time is ' + time)

        # Open websites ---
        elif 'open google' in command:
            say('Opening Google')
            webbrowser.open('https://www.google.com')

        elif 'open youtube' in command:
            say('Opening YouTube')
            webbrowser.open('https://www.youtube.com')

        elif 'open instagram' in command:
            say('Opening Instagram')
            webbrowser.open('https://www.instagram.com')

        elif 'open gmail' in command:
            say('Opening Gmail')
            webbrowser.open('https://mail.google.com')

        elif 'open github' in command:
            say('Opening GitHub')
            webbrowser.open('https://github.com')

        #  Open applications ---
        elif 'open notepad' in command:
            say('Opening Notepad')
            os.system('notepad')

        elif 'open calculator' in command:
            say('Opening Calculator')
            os.system('calc')

        elif 'open chrome' in command:
            say('Opening Google Chrome')
            os.system('start chrome')

        # --- Play music ---
        elif 'play music' in command:
            say('Playing music')
            music_path = "C:\\Users\\VICTUS\\Downloads\\videoplayback (3).m4a"  # Change path if needed
            os.startfile(music_path)
           

        elif 'exit' in command or 'stop' in command:
            say('Goodbye!')
            break

        elif command:
            say("Sorry, I didn't understand that. Please say again.")


run_assistant()
