from deep_translator import MyMemoryTranslator
"""
    Translating english to french
"""
def english_to_french(english_text):
    translator = MyMemoryTranslator(src='en', dest='fr')
    french_text = translator.translate(english_text)
    return french_text

"""
    Translating french to english
"""
def french_to_english(french_text):
    translator = MyMemoryTranslator(src='fr', dest='en')
    english_text = translator.translate(french_text)
    return english_text

