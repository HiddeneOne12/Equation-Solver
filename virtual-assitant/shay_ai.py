from gtts import gTTS
import os
import datetime
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import webbrowser
import subprocess
import subprocess, sys,platform
# import openai

# client = openai()

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "assassins creed"
#         }
#       ]
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
#   response_format={
#     "type": "text"
#   }
# ) 
all_websites = [
    {'name' : 'Youtube'.lower() , 'url' :  'https://www.youtube.com'},
    {'name' : 'Google'.lower() , 'url' :  'https://www.google.com'},
    {'name' : 'Wikipedia'.lower() , 'url' :  'https://www.wikipedia.com'},
    {'name' : 'Github'.lower() , 'url' :  'https://www.github.com'},
    {'name' : 'Whatsapp'.lower() , 'url' :  'https://web.whatsapp.com'},
    {'name' : 'Stack Overflow'.lower() , 'url' :  'https://stackoverflow.com'},
    {'name' : 'Chat Gpt'.lower() , 'url' :  'https://chatgpt.com'},
    {'name' : 'Virtual University'.lower() , 'url' :  'https://vulms.vu.edu.pk'},
    {'name' : 'Ocean of Games'.lower() , 'url' :  'https://oceansofgamess.com'},
  
]

all_apps = [
      {'name' : 'Visual Studio'.lower() , 'path' :  '/Applications/Visual Studio Code.app'},
      {'name' : 'Android Studio'.lower() , 'path' :  '/Applications/Android Studio 2.app'},
      {'name' : 'Any Desk'.lower() , 'path' :  '/Applications/AnyDesk.app'},
      {'name' : 'Postman'.lower() , 'path' :  '/Applications/Postman.app'},
      {'name' : 'Zoom'.lower() , 'path' :  '/Applications/zoom.us.app'},
      {'name' : 'App Store'.lower() , 'path' :  '/System/Applications/App Store.app'},
      {'name' : 'Meeting'.lower() , 'path' :  '/Applications/Microsoft Teams.app'},
      {'name' : 'Email'.lower() , 'path' :  '/System/Applications/Mail.app'},
      {'name' : 'X Code'.lower() , 'path' :  '/Applications/Xcode.app'},
      {'name' : 'Downloads'.lower() , 'path' :  '/Users/apple/Downloads/'},
      {'name' : 'Github Projects'.lower() , 'path' :  '/Users/apple/GitHub'},
      {'name' : 'Flutter Projects'.lower() , 'path' :  '/Users/apple/AndroidStudioProjects'},
      {'name' : 'Flutter Version'.lower() , 'path' :  '/Users/apple/FlutterVersion'},
      {'name' : 'Python Projects'.lower() , 'path' :  '/Users/apple/python-projects'},
      {'name' : 'C++ Projects'.lower() , 'path' :  '/Users/apple/c++-projects'},
      {'name' : 'Music'.lower() , 'path' :  '/System/Applications/Music.app'},
      {'name' : 'Settings'.lower() , 'path' :  '/System/Applications/System Settings.app'},
      {'name' : 'Photos'.lower() , 'path' :  '/System/Applications/Photos.app'},
      {'name' : 'Notepad'.lower() , 'path' :  '/System/Applications/Notes.app'},
      {'name' : 'Terminal'.lower() , 'path' :  '/System/Applications/Utilities/Terminal.app'},      
]



# Converting Text into Audio / Voice
def speak(audio):
    
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")
    
# Greet the user based on the time of day.
def greet_user():

    hour = int(datetime.datetime.now().hour)
    
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
   
    speak("Hello Abdullah how can i help you today")

# Listen for a command from the user.  
def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-pk')
        print(f'User said : {query}\n')
        
    except Exception as e:
        
        print(f"Error : {e}")
        print("Failed to Identify.....")
        speak('failed to identify please speak again')
        return "None"
    
    return query
        
if __name__ == "__main__":

    greet_user()
    while True:        
     query =  take_command().lower()
     
     if 'search'.lower() in query:
         speak("Searching Wikipedia")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         print(results)
         speak(results)
         
     elif 'play'.lower() in query:
        song = query.replace('play', '')
        speak(f'Playing {song} on YouTube')
        pywhatkit.playonyt(song)
        
     elif 'time'.lower() in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        
     elif 'open'.lower() in query:
        for website in all_websites:           
            if website['name'].lower() in query:
                speak(f"Opening {website['name'].title()}...")
                webbrowser.open(website['url'])
                
     elif 'app'.lower() in query or 'projects'.lower() in query or 'downloads'.lower() in query or 'version'.lower() in query:
            for app in all_apps:           
              if app['name'].lower() in query:
                speak(f"Opening {app['name'].title()}...")
                if platform.system() == "Windows":
                  os.startfile(app['path'])
                else:
                  opener = "open" if sys.platform == "darwin" else "xdg-open"
                  subprocess.call([opener, app['path']])
                                  
     elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a nice day!")
        exit()
       
