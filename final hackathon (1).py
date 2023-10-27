#!/usr/bin/env python
# coding: utf-8

# In[16]:


import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import numpy as np
import pyttsx3
import apikey


engine=pyttsx3.init()
engine.say('Hello I am Sara')
engine.say('How May I help U today')
engine.runAndWait()


openai.api_key = "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"


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    
    chatStr += f"syntaxslayer: {query}\n Sara: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')
if __name__ == '__main__':
    print('hello')
    say("Hello I am Sara")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Sara"

if __name__ == '__main__':
    print('Welcome to Sara')
    say("Sara")
    while True:
        print("Listening...")
        query = takeCommand()
       
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["Medical help", "https://www.webmd.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "Depression" in query:
            print("call/whatsapp +91-9999666555")

        elif "obesity" in query:
            url = "https://www.webmd.com/obesity/what-obesity-is"
            webbrowser.open(url)


        elif "diabetes".lower() in query.lower():
            url = "https://www.webmd.com/diabetes/understanding-diabetes-symptoms"
            webbrowser.open(url)

        elif "Malaria".lower() in query.lower():
            url = "https://www.webmd.com/a-to-z-guides/malaria"
            webbrowser.open(url)

        elif "Cancer".lower() in query.lower():
            url = "https://www.webmd.com/cancer/understanding-cancer-symptoms"
            webbrowser.open(url)

        elif "Sara Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("chatting...")
            chat(query)
            #say(query)


# In[ ]:





# In[ ]:





# In[ ]:




