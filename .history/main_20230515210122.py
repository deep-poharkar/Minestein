import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say " + text)
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            
            return query
        
        except Exception as e:
            return "Pardon please repeat again..."
            
        
   
    
if __name__ == '__main__':
    print('Minestein')
    say("Minestein")
    while True:
        print("Listening...")
        query = takeCommand()
        
    # say(query)