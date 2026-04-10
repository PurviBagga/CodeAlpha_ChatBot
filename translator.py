from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def home():
    return "Translator is running!"

@app.route("/translate/<text>")
def translate(text):
    result = translator.translate(text, dest='hi')
    return result.text

app.run(debug=True)