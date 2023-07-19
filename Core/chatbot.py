from flask import Flask, request, jsonify

import requests



app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = process_message(message)
    return jsonify({'response': response})

@app.route('/')
def home():
	return "Hello! this is the main page <h1>HELLO</h1> "


def process_message(message):
    # Add your AI chatbot logic here
    # You can use any NLP or machine learning libraries, such as spaCy, NLTK, or TensorFlow
    # For simplicity, let's just echo the user's message
    #  as the response

    print("Request recieved!!")


if __name__ == '__main__':
    app.run(debug=True)
