import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say " + text)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            return query
            
        except Exception as e:
            return "Pardon me, please say that again"
            
        
   
    
if __name__ == "__main__":
    
    say("Hello, I am your personal Einstein.")
    while True:
        print("Listening...") 
        query = takeCommand()
if "Open YouTube".lower() in query.lower():
        say ("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        
    # say(query)