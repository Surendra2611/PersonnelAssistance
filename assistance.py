import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

  hour = int(datetime.datetime.now().hour)
  print(hour)
  if hour>=0 and hour<12:
      speak('Good morning sir!')

  elif hour>=12 and hour<16:
      speak('Good afternoon sir!')

  else:
      speak('Good evening sir!')


  speak('I am your Personnel Assistance, how may i help you')

def userInput():
    #will take user command
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio,Language='en.in')
        print(f"User Said:{query}\n")
    except Exception as e:
       # print(e)
        print('Say that again.... , i didnt get')
        speak("say that again....,i didn't get")
        return "None"
    return query



if __name__ == '__main__':
    speak('hello welcome sir')
    wishMe()
    while True:
          query = userInput().lower()
          # logic for executing task based on query
          if 'wikipedia' in query:
              speak('Searching wikipedia....')
              query = query.replace('wikipedia','')
              results = wikipedia.summary(query,sentences=2)
              speak('According to wikipedia')
              print(results)
              speak(results)

          elif 'open youtube' in query:
              webbrowser.open('youtube.com')
          elif 'open google' in query:
              webbrowser.open('google.com')

          elif 'open code' in query:
            path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.2.3\\bin\\idea64.exe"
            os.startfile(path)

          elif 'open firefox' in query:
              path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
              os.startfile(path)

          elif 'time' in query:
              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"Sir,the time is{strTime}")

          elif 'quit' in query:
              speak("Okay thank you very much sir,connect with me whenever thers is need")
              exit()
