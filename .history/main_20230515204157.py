import speech_recognition as sr
import os


def say(text):
    os.system("say " + text)
    say("Hello, I am your personal assistant. What can I do for you?")