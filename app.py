from flask import Flask, request, jsonify

app = Flask(__name__)

# Questions and answers (your chatbot brain 🧠)
faqs = {
    "what is ai": "AI means Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "who are you": "I am your chatbot made for CodeAlpha task.",
    "hello": "Hi! How can I help you?"
}

def get_response(user_input):
    user_input = user_input.lower()
    for question in faqs:
        if question in user_input:
            return faqs[question]
    return "Sorry, I don't understand."

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

@app.route("/test/<msg>")
def test(msg):
    response = get_response(msg)
    return response

app.run(debug=True)