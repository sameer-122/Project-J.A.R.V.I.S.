import speech_recognition as sr
from googletrans import Translator
from langdetect import detect     # this module is very bad in detecting languages, try  'Google Cloud Translation API'
import pyttsx3

engine = pyttsx3.init('sapi5')  # sapi5 is an api of windows to use inbuilt voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)

            print('Recognizing...')
            query = r.recognize_google(audio, language='en-IN')
            print(f'user said: {query}')

            language = detect(query)
            print(language)

            if language != 'en':
                print('Translating..')
                query = Translator().translate(query, src='hi', dest='en').text

    except Exception as e:
        print(f'error: {e}')




    print(query)
    return query

if __name__ =='__main__':
    print('hi')
    q = listen()
    speak(q)