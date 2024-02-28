import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import requests
import random

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

# Define a function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

# Define your assistant's actions
def assistant(query):
    
    if "search" in query:
        speak("What would you like to search for?")
        search_query = listen()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
    elif "play" in query:
        song = query.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
   
    elif "joke" in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why don't skeletons fight each other? They don't have the guts."
        ]
        joke = random.choice(jokes)
        speak(joke)
    elif "website" in query:
        speak("Which website would you like me to open?")
        website = listen()
        url = f"http://durvankursonar.me"
        webbrowser.open(url)
    elif "exit" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to help with that.")

# Main loop
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()
        assistant(query)
