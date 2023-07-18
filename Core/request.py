import requests


url = 'http://localhost:5000/chat'
myobj = {'message': 'Hello, chatbot!'}

x = requests.post(url, json = myobj)

print(x.text)