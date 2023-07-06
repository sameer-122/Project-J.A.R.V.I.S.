# you can use Google Cloud Natural Language API ,if cost is no issue
# use Google Cloud Translation API
from langdetect import detect
import spacy

def detect_language_spacy(text):
    nlp = spacy.load('xx_ent_wiki_sm')
    doc = nlp(text)
    if doc._.language:
        return doc._.language['language']
    else:
        return None

def detect_language_lang(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        print(f"Language detection error: {e}")
        return None

if __name__ == "__main__":
    # Text examples
    texts = [
        "Hello, how are you?",
        "Bonjour, comment ça va ?",
        "你好，最近怎么样？",
        "Hola, ¿cómo estás?"
    ]


    for text in texts:
        language = detect_language_lang(text)
        if language:
            print(f"Text: '{text}'\tLanguage: {language}")
        else:
            print(f"Failed to detect language for text: '{text}'")
