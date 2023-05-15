import speech_recognition as sr
import os


def say(text):
    os.system("say " + text)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            
        except Exception as e:
            say("Pardon me, please say that again")
            return "None"
        
        return query    
    
if __name__ == "__main__":
    
    say("Hello, I am your personal Einstein.")
    print("Listening...") 
    text = takeCommand()
    say(text)