import pyttsx3                                   #install in Cmd : pip install pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()