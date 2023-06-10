ijofrom turtle import goto
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser
import os
import random
from jarvis_mail import sendEmail
from fuzzywuzzy import fuzz

email_dict = {'to wasim':'wasim.alam100@gmail.com', 'to sameer':'sameer.alam100@gmail.com' }
s = ' '*40

engine = pyttsx3.init('sapi5')  # sapi5 is an api of windows to use inbuilt voice

voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <=12:
        speak("Good Morning !")

    elif hour >= 12 and hour <=18:
        speak("Good Afternoon !")

    else:
        speak("Good Night !")

    speak("I am Jarvis Sir, Please tell me How may I help you")


def takeCommand():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()                    # Creating "r" as an object/instance of Recognizer class
    with sr.Microphone() as source:        # The sr.Microphone() creates an instance of the Microphone class from the SpeechRecognition library, which represents the microphone as the audio source.
        print("Listening..."+s, end='\r')              # Microphone and Recognizer both inherits AudioSource class
        r.pause_threshold = 1.5
        r.energy_threshold = 300
        
        audio = r.listen(source)           # code starts listening

    try:
        print('Recognizing...'+s, end='\r')
        query = r.recognize_google(audio, language='en-in')      # converts audio to string
        print(f'User said: {query}')
        query = query.lower()
        
        if fuzzmatch('quit',query):
            print('Quitting')
            speak('Quitting')
            exit()

    except Exception as e:
        # print(e)
        print('\rAudio energy  low,'+s, end='\r')
        speak('audio energy low')
        return takeCommand()
    
    return query

def fuzzmatch(desired_phrase, query):
    q = query
    ln= len(desired_phrase)
    max_ratio=0
    for i in range(len(q)):
        if i+ln > len(q) and i!=0 : 
            # print(f'fuzmatch failed: {max_ratio}')
            return False
        phrase= q[i:i+ln]
        similarity_ratio = fuzz.ratio(desired_phrase,phrase)
        max_ratio = max(max_ratio, similarity_ratio)
        if similarity_ratio > 60:
            # print(f'fuzmatch passed: {similarity_ratio}')
            return True        



if __name__ == "__main__":
    # wishme()                    speak("Worship the creator, Not the creation")
    # while True:

    def act():
        query = takeCommand()
        q = query
        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('serching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com',1)

        elif ('stack overflow' in q) or ('stackoverflow' in q):
            # webbrowser.register('chrome',None)
            print(results)
            webbrowser.open('stackoverflow.com')

        elif ('play' in q) and ('music' in q or 'the way' in q) :
            music_dir = 'D:\\Nasheed'
            songs = os.listdir(music_dir)
            print(songs)
            if 'the way' in query:   
                os.startfile(os.path.join( music_dir, 'the-way-of-the-tears.mp3') )    
            else:   
                id = random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_dir, songs[id]))
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strTime}')

        elif 'open code' in query:
            codePath = r'C:\Users\syeds\AppData\Local\Programs\Microsoft VS Code\Code.exe' 
            os.startfile(codePath)

        elif  'mail to' in q or 'email to' in q or 'male to' in q or 'mel to' in q:

            to = 'none'
            found = False
            max_match = 0

            for key in email_dict.keys():
                ln= len(key)
                for i in range(len(q)):
                    if i+ln > len(q) : break
                    phrase= q[i:i+ln]
                    similarity_ratio = fuzz.ratio(key,phrase)
                    max_match = max(max_match, similarity_ratio)
                    if similarity_ratio > 60:
                        to = email_dict[key]
                        found = True
                        break            
                if found == True:        break

            print('Match :', max_match)

            if to == 'none':
                speak('Sir, The receiver of this mail is not present in the email directory. Please update the directory, or mention it again')
                act()
                return
            
            try:
                speak('What should I say')
                content = takeCommand()

                sendEmail(to, content)
                speak('Email has been sent! Sir')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email, there is some technical glitch!')

        else:
            speak('I didn\'t get you, Can you come again')
            act()
        act()
    act()       


  