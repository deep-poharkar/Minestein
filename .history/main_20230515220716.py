import datetime
import speech_recognition as sr
import os
import webbrowser
import openai

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response to prompt: {prompt}\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write a tagline",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    print(response["choices"][0]["text"])
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"prompt - {random.randint(1, 100000)}", "w") as f:
        f.write(text)


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
              
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The time is {strfTime}") 
                
            if "open facetime" in query.lower():
                say("Opening facetime now")
                os.system(f"open /System/Applications/FaceTime.app")
                
            if "Using A.I" in query.lower():
                ai(prompt=query)
                os.system(f"open https://beta.openai.com")
        
    # say(query)