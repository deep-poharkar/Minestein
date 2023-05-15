import speech_recognition as sr
import os


def say(text):
    os.system("say " + text)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
            
        except Exception as e:
            say("Pardon me, please say that again")
            return "None"
        
        return statement    
    
if __name__ == "__main__":
    
    say("Hello, I am your personal Einstein.")