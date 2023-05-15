import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say " + text)
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            return query
            
        except Exception as e:
            say("Pardon me, please say that again")
            
        
   
    
if __name__ == "__main__":
    
    say("Hey, I am your personal Einstein.")
    while True:
        print("Listening...") 
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["stackoverflow", "https://www.stackoverflow.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
              say("Opening {site[0]} now")
              webbrowser.open(site[1])
        
    # say(query)