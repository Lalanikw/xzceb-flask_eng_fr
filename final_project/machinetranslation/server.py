from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(text_to_translate)
    return "Translated text to French"

@app.route("/french_to_fnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(text_to_translate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

 if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
