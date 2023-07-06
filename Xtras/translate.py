from googletrans import Translator




if __name__ == '__main__':
    texts = ["तेज, भूरी लोमडी आलसी कुत्ते के उपर कूद गई।","משפטים אקראיים בעברית","Je suis dans une réunion française maintenant",
             "Привет, как дела","שלום עולם!", "مرحبا بالعالم!", "こんにちは世界!"]
    translator = Translator()

    # for text in texts:
    #     translation = translator.translate(text, dest="en")
    #     print(translation.text)
    sentences = [
        "मेरा नाम जॉन है।",
        "मुझे यह समझ नहीं आ रहा है।",
        "मैं भारत से हूँ।",
        "आप कैसे हैं?",
        "मुझे भूख लगी है।",
        "क्या आपको मदद चाहिए?",
        "आपका स्वागत है।",
        "कृपया मुझे माफ़ करें।",
        "धन्यवाद।"
    ]
    joined_String = ','.join(sentences)
    print(joined_String)
    translation = translator.translate(joined_String, dest='en')
    print(translation.text)

















# print('  __\n /__)  _  _     _   _ _/   _\n/ (   (- (/ (/ (- _)  /  _)\n         /')
# lis = [x*x for x in range(10)]
# for i,x in enumerate(lis):
#     print(f'{i} :{x}')