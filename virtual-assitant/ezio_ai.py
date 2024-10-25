from gtts import gTTS
import os
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import webbrowser

def speak(text):
    """Convert text to speech using gTTS."""
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # 'afplay' is a command to play audio files on macOS

def greet_user():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Welcome back How can i be of your service today")

def take_command(command):
    """Listen for a command from the user."""
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)
    
    if(command != ''):        
        try:
            print("Recognizing...")
            query = command
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

def perform_task(query):
    """Perform a task based on the user's command."""
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=15)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'play' in query:
        song = query.replace('play', '')
        speak(f'Playing {song} on YouTube')
        pywhatkit.playonyt(song)
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open' in query:
        speak(f"{query}")
        os.system(query)    
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a nice day!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")
    query = 'None'    

if __name__ == "__main__":
    greet_user()
    query = input("Enter User Command")
    while True:
        if(query != ''):
              perform_task(query)
              query=  input("Enter User Command")
    
      
          
