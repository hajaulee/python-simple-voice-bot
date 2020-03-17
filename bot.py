import requests
import json
from gtts import gTTS
import os
import speech_recognition as sr 
sample_rate = 48000
chunk_size = 2048


def bot_rep(text):
#     text = 'ok mày giỏi, thế biết mai có mưa không'
    url = 'https://sim.vuiz.net/post_sim.php'
    obj = {'hoi': text, 'lang':'vi'}
    x = requests.post(url, data = obj)

    data = json.loads(x.text)
    reply = data['message'].strip()
    return reply

def print_and_speak(text, lang='vi'):
    print("Bot:", text)
    tts = gTTS(text, lang=lang)
    tts.save('hello.mp3')
    os.system("mpg123 hello.mp3") 


r = sr.Recognizer() 
  
#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
  
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
# for i, microphone_name in enumerate(mic_list): 
#     print(microphone_name)

device_id = 7
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 

text = ""
while "dừng lại" not in text:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                            chunk_size = chunk_size) as source: 
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        print ("Bạn:", end="")
        #listens for the user's input 
        audio = r.listen(source) 

        try: 
            text = r.recognize_google(audio, language='vi-VN') 
            print (text)
            reply = bot_rep(text)
            print_and_speak(reply)
        #error occurs when google could not understand what was said 

        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
#             print("")
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

print_and_speak("Hẹn gặp bạn lần sau")
os.system('exit')