import speech_recognition as sr                     #install in Cmd : pip install SpeechRecognition
from requests_html import HTMLSession               #install in Cmd : pip install PyAudio
import text_to_speech


def spech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
       audio = r.listen(source)    #methord
       voice_data = ''
       try:
        voice_data = r.recognize_google(audio)
        return voice_data

       except sr.UnknownValueError:
         text_to_speech.speak("sorry")
       except sr.RequestError:
            text_to_speech.speak('No internet connect please turn on you internet')


