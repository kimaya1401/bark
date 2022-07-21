import datetime
import wikipedia
import pyjokes
import speech_recognition as sr
import pywhatkit
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Hello, how may I help you?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run():
    do=take_command()
    if 'time' in do:
        time= datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
    elif 'joke' in do:
        talk(pyjokes.get_joke())
    elif 'are you single' in do:
        talk('I am in a relationship with wifi')
    elif 'who are you' in do:
        talk('I am Bark. Your Assistant')
    elif 'play' in do:
        song = do.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'who is' in do:
        person = do.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)



while True:
    run()