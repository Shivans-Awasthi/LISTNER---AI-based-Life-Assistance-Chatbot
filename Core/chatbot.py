from flask import Flask, request, jsonify
from flask import Flask, render_template, request, url_for, flash, redirect
from bardapi import Bard

app = Flask(__name__)


@app.route('/', methods=['GET'] )
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'] )
def chat():
    # message = request.json['message'] 
    message=request.form['message']
    response = process_message(message)
    return render_template("index.html", result=response)


def process_message(message):
    # Add your AI chatbot logic here
    # You can use any NLP or machine learning libraries, such as spaCy, NLTK, or TensorFlow
    # For simplicity, let's just echo the user's message
    #  as the response
    token = 'ZAiiurgYOr0_6EtTusLvjWlAuDjqs8gD3Susel3iz1Em0jDXf-OvJIcTIoTOf2KhD-k_xQ.'
    input_text = request.form['message']
    bard = Bard(token=token)
    botmessage = bard.get_answer(input_text)['content']

    return botmessage



if __name__ == '__main__':
    app.run(debug=True)
