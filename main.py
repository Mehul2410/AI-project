import pyttsx3 as p
import speech_recognition as sr
from maps import maps
from meet import meet
from news import *
from jokes import *
from seleniumweb import infow
from yt_auto import music
import randfacts
import requests
from weather import *
from ss import *
import time

engine = p.init()
rate= engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def randjoke():
    speak("Sure sir")
    fun = joke()
    print(fun)
    speak(fun)
    speak('Hello sir, should i share some more joke?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            jokes = r.recognize_google(audio)    
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
        if "more" and "yes" in jokes:
            randjoke()
        else:
            speak("Okay sir")

def weatherupdate():
    speak('of which city you want to know the weather?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        city = r.recognize_google(audio)
        print(city)
    api_address  ='https://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=' + weather
    json_data = requests.get(api_address).json()
    temprature = temp(json_data)
    desc = des(json_data)
    speak('hello sir temprature in {} is {} and with {}'.format(city,temprature,desc))
    speak('Hello sir, would you like to know weather update about different city?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            nextweather = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
    if "more" and "yes" in nextweather:
        speak('Sure sir')
        weatherupdate()
    else:
        speak("Okay sir")

def randfact():
    x = randfacts.getFact()
    print(x)
    speak('Did you know that, '+x)
    speak('Hello sir, should i share some more facts?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            facts = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
    if "more" and "yes" in facts:
        speak('Sure sir')
        randfact()
    else:
        print(facts)
        speak("Okay sir")

  
r = sr.Recognizer()
speak('Hello sir i am your voice assistant. How are you?')

with sr.Microphone() as source:
    r.energy_threshold  =10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening...')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        speak("Assistant could not understand the audio")
    except sr.RequestError as ex:
        speak("Request Error from Google Speech Recognition " + ex)

if "what" and "about" and "you" in text:
    speak('I am also having a good day sir')
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold  =10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening....')
    audio= r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

def more():
    speak("what else can i do for you?")
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening....')
        audio= r.listen(source)
        try:
            text2 = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
        
    return text2

if 'information' in text2:
    speak('You need information related to which topic?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            infor = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
        print(infor)
    speak('searching {} in wikipedia'.format(infor))
    assist = infow()
    assist.get_info(infor)
elif "meet" in text2:
    googlemeet = meet()
    googlemeet.get_info()
    speak('Your meet is ready sir')
    # text2= more()
    # print(text2)
elif "Map" in text2:
    speak('Which location you want to see')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            location = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
    speak("Showing result for {} location".format(location))
    gmap = maps()
    gmap.get_info(location)
elif "video" in text2:
    speak('what do you want me to play for you?')
    with sr.Microphone() as source:
        r.energy_threshold  =10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            vid = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Assistant could not understand the audio")
        except sr.RequestError as ex:
            speak("Request Error from Google Speech Recognition " + ex)
    speak("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "weather" in text2:
    weatherupdate()

elif "news" in text2:
    print('Sure sir, Now i will read news for you.')
    speak('Sure sir, Now i will read news for you.')
    arr = news()
    for i in arr:
        print(i)
        speak(i)
        
elif "fact" in text2:
    randfact()
    
elif "joke" in text2:
    randjoke()
