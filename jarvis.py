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
import subprocess
import sys
import openai
from config import openAi_api_key

starline = '*' * 100

def cv_mod(query):
    with open('CV/origiinal_cv.txt', 'r') as f:
        text=f.read()
    prompt = query + '\n current CV: \n ' + text
    print(prompt)
    openai.api_key = openAi_api_key

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(starline,'\n',response['choices'][0]['text'])
    if not os.path.exists("CV"):
        os.mkdir("CV")
    with open(f"CV/{query}.txt  ", 'w') as f:
        f.write(response['choices'][0]['text'])

chatStr=''
def chat(query):
    global chatStr
    openai.api_key = openAi_api_key
    chatStr += f"Sameer: {query}\nJarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatStr += f"{response['choices'][0]['text']}"
    print(chatStr)
    speak(response['choices'][0]['text'])
    return response['choices'][0]['text']


def ai(prompt):
    # prompt = ''.join(prompt.split('intelligence')[1:]).strip()
    openai.api_key = openAi_api_key

    text = f"OpenAI response for prompt: {prompt} \n ******************************** \n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : warp this inside try catch
    print(starline)
    print(f'Prompt: {prompt}')
    print(response['choices'][0]['text'])
    print(starline)

    text += response['choices'][0]['text']

    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{prompt}.txt  ", 'w') as f:
        f.write(text)



email_dict = {'to wasim': 'wasim.alam100@gmail.com', 'to sameer': 'sameer.alam100@gmail.com'}
s = ' ' * 40

engine = pyttsx3.init('sapi5')  # sapi5 is an api of windows to use inbuilt voice

voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <= 12:
        speak("Good Morning !")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon !")

    else:
        speak("Good Night !")

    speak("I am Jarvis Sir, Please tell me How may I help you")


def takeCommand(retry_count=3):
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()  # Creating "r" as an object/instance of Recognizer class
    with sr.Microphone() as source:  # The sr.Microphone() creates an instance of the Microphone class from the SpeechRecognition library, which represents the microphone as the audio source.
        r.pause_threshold = 1.2  # Microphone and Recognizer both inherits AudioSource class
        r.energy_threshold = 300

        print("Listening..." + s, end='\n')
        # speak('Listening')
        audio = r.listen(source)  # code starts listening

    try:
        print('Recognizing...' + s, end='\n')
        query = r.recognize_google(audio, language='en-in', pfilter=0)  # converts audio to string (en-in,hi-in)
        print(f'User said: {query}')
        query = query.lower()

    except Exception as e:
        # print(e)
        print('Audio energy  low,' + s, end='\n')
        speak('audio energy low')
        if retry_count > 0:
            return takeCommand(retry_count - 1)
        else:
            print('No Response. Quitting !')
            exit()

    return query


def fuzzmatch(desired_phrase, query, cutoff_ratio=60, text=''.strip()):
    if text: text ='for '+text
    q = query
    ln = len(desired_phrase)
    max_ratio = 0
    for i in range(len(q)):
        if i + ln > len(q) and i != 0:
            # print(f'fuzzmatch failed {text}: {max_ratio}')
            return False
        phrase = q[i : i+ln]
        similarity_ratio = fuzz.ratio(desired_phrase, phrase)
        max_ratio = max(max_ratio, similarity_ratio)
        if similarity_ratio >= cutoff_ratio:
            print(f'fuzzmatch passed {text}: {similarity_ratio}')
            return True


if __name__ == "__main__":
    # wishme()   
    # speak('jaaarvis , A eye')                          # speak("Worship the creator, Not the creation")
    while True:

        query = takeCommand().lower()
        q = query

        if 'wikipedia' in query and not ('open' in query):
            speak('serching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        sites = [['youtube', 'youtube.com'], ['google', 'google.com'], ['stack overflow', 'stackoverflow.com'],
                 ['wikipedia', 'wikipedia.org']]
        chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        for site in sites:
            if f"open {site[0]}" in query:
                subprocess.call([chromePath,site[1]])
                # webbrowser.open(site[1])
                speak(f"Opening {site[0]}")

        # todo : Add a feature to play every song if specified by name
        if ('play' in q) and ('music' in q or 'the way' in q):
            music_dir = 'D:\\Nasheed'

            songs = os.listdir(music_dir)
            print(songs)

            # import subprocess
            # import sys

            # filename = "path/to/your/file"  # Replace with the actual path of the file you want to open

            # if sys.platform == "darwin":
            #     opener = "open"
            # elif sys.platform == "win32":
            #     opener = "start"
            # else:
            #     opener = "xdg-open"
            #
            # subprocess.call([opener, music_dir])

            if 'the way' in query:
                os.startfile(os.path.join(music_dir, 'the-way-of-the-tears.mp3'))
            else:
                id = random.randint(0, len(songs) - 1)
                os.startfile(os.path.join(music_dir, songs[id]))  # os.startfile() function of os module

            exit()  # making it exit() since it will respond to music

        elif 'the time' in query:
            # strTime = datetime.datetime.now().strftime('%H:%M:%S')
            hour = int(datetime.datetime.now().strftime('%H'))
            min = datetime.datetime.now().strftime('%M')

            timePeriod = 'pm' if hour >= 12 else 'am'
            hour = hour - 12 if hour >= 13 else hour
            speak(f'Sir the time is {hour} {min} {timePeriod}')

        # todo : Add a feature to open any app in windows with help of dictionary
        elif 'open ' in query:
            dic = {'code':r'C:\Users\syeds\AppData\Local\Programs\Microsoft VS Code\Code.exe',
                   'chrome':r"C:\Program Files\Google\Chrome\Application\chrome.exe"}
            for key in dic.keys():
                if key in query:
                    codePath = dic[key]
                    subprocess.Popen(codePath)
                    break

            # os.startfile(codePath)                # you can use either of 3 command to start.
            # os.system(f'"{codePath}"')
            # subprocess.Popen(codePath)


        elif 'using' not in q and ('mail to' in q or 'email to' in q or 'male to' in q or 'mel to' in q):
            to = 'none'
            for key in email_dict.keys():
                if fuzzmatch(key,query,cutoff_ratio=60):
                    to = email_dict[key]

            if to == 'none':
                speak(
                    'Sir, The receiver of this mail is not present in the email directory. Please update the directory, or mention it again')
                continue

            try:
                speak('What should I say')
                content = takeCommand()

                sendEmail(to, content)
                speak('Email has been sent! Sir')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email, there is some technical glitch!')

        elif 'sms' in query:
            from jarvis_sms import sms
            speak('what should I say')
            body = takeCommand()
            sms(body)

        elif 'write' in q or 'using intelligence' in q or 'intelligence' in q :
            ai(prompt=q)

        elif ' cv ' in q:
            cv_mod(q)

        elif 'reset chat' in query:
            chatStr = ''

        elif  'exit' in query or 'quit' in query or fuzzmatch('quit', query, cutoff_ratio=76, text='quit'):
            print('Quitting')
            speak('Quitting')
            exit()
        break
        # else:
        #     print('chatting')
        #     chat(query)
