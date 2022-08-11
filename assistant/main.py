import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) 
            command = command.lower()
            if 'lilith' in command:
                command = command.replace('lilith', '')
                print(command)
    except:
        pass
    return command


def run_lilith():
    command = take_command()
    print(command)
    if 'close' in command:
        exit()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'youtube' in command:
        talk('opening youtube')
        get_url=webbrowser.open('https://www.youtube.com/')
    elif 'google' in command:
        talk('opening google')
        get_url=webbrowser.open('https://www.google.com/')
    elif 'github' in command:
        talk('opening github')
        get_url=webbrowser.open('https://www.github.com/')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'how are you' in command:
        talk('i am fine thanks')
        print('i am fine thanks')
    elif 'who are you' in command:
        talk('I was created by life, i am lilith and i love my job')
        print('I was created by life, i am lilith and i love my job')
    elif 'kimsin' in command:
        talk('Life tarafından üretildim')
        print('Life tarafından üretildim')
    else:
        talk('Please say the command again.')
         


while True:
    run_lilith()