from googletrans import Translator

trans = Translator()

def translateToEn(text):
    textTranslated = trans.translate(text, dest="en")
    print(textTranslated.text)
    return textTranslated.text


def discoverLang(text):
    langDetected = trans.detect(text)
    return langDetected.lang
