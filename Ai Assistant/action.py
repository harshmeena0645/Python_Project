import datetime
import text_to_speech
import webbrowser
import weather
import os


def Action(send) :

    data_btn  = send.lower()

    if "what is your name" in   data_btn :
        text_to_speech.speak("my name is AI Assitant")
        return "my name is AI Assitant"

    elif "hello" in data_btn  or "hii" in data_btn  or "hey" in data_btn or "hi" in data_btn:
        text_to_speech.speak("Hey sir, How i can  help you !")
        return "Hey sir, How i can  help you !"

    elif "how are you" in  data_btn :
        text_to_speech.speak("I am doing great these days sir")
        return "I am doing great these days sir"
    
    elif "who is your owner" in  data_btn :
        text_to_speech.speak("My Owner is Harsh")
        return "My Owner is Harsh"
    
    elif "tell me about harsh" in  data_btn :
        text_to_speech.speak("Harsh is Great")
        return "Harsh is Great"

    elif "thanku" in data_btn or "thanks" in data_btn:
        text_to_speech.speak("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"

    elif "good morning" in data_btn:
        text_to_speech.speak("Good morning sir, i think you might need some help")
        return "Good morning sir, i think you might need some help"

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute"
        text_to_speech.speak(Time)
        return str(Time)

    elif "shutdown" in data_btn or "quit" in data_btn:
            text_to_speech.speak("ok sir")
            return "ok sir"

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        text_to_speech.speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"

    elif 'google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        text_to_speech.speak("google open")
        return "google open"
    
    elif 'chrome' in data_btn or 'chrome'  in data_btn:
        url = 'https://chrome.com/'
        webbrowser.get().open(url)
        text_to_speech.speak("chrome open")
        return "chrome open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        text_to_speech.speak("YouTube open")
        return "YouTube open"
    
    elif 'weather' in data_btn :
        ans   = weather.weather()
        text_to_speech.speak(ans)
        return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.speak("songs playing...")
        return "songs playing..."

    else :
        text_to_speech.speak( "i'm able to understand!")
        return "i'm able to understand!"
