import pyttsx3
import speech_recognition as sr
from bardapi import Bard
# import pyaudio

  # Enter your API key from your OpenAI account

token = 'awiiuqxNOJ_B15dI_L-UZYyuGgsoVrB_kuMG5hUmHsE-3iPTZ0iCRQsRXM58_ao8S4ZIog.'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"User said: {query}\n ")

        except Exception as e:
            print(e)
            print("say that again please...")
            return "NULL"
        return query
    
    
def chatgpt(query):
        # response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        # messages=[
        #     {"role": "system", "content": "You are a Virtual Assistant "},
        #     {"role": "user", "content": query },
        #          ]
        # )

        # result = ''
        # for choice in response.choices:
        #     result += choice.message.content
    
        #     print(result)
        #     speak(result)

        
        input_text = "hello"
        bard = Bard(token=token)
        botmessage = bard.get_answer(input_text)['content']
        print(botmessage)
        speak(botmessage)
       


# while(1):
#     # query = takecommand().lower()  #comment this line and
#     query = " hi I am Jack"       # Uncomment this if you want to give written instructions
#     # if 'hello' in query:
#     #     query = query.replace("hello", "")
#     #     chatgpt(query)
#     # elif 'hi' in query:
#     #     query = query.replace("jarvis", "")
#     chatgpt(query)
        
query = " hi I am Jack"       # Uncomment this if you want to give written instructions
    # if 'hello' in query:
    #     query = query.replace("hello", "")
    #     chatgpt(query)
    # elif 'hi' in query:
    #     query = query.replace("jarvis", "")
chatgpt(query)





# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

# import assemblyai as aai

# aai.settings.api_key = "daef524105fc4121927b232176ec520a"
# transcriber = aai.Transcriber()

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# print(transcript.text)