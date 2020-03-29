#installing requried module if u have the module then u dont need to install
# pip install pyttsx3,SpeechRecoginition,wikipedia,pywin32,pyaudio,pywin32

# import modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5') # sap15 is Microsoft speech api
voices = engine.getProperty('voices') # getting the property
# we gonno seet some property for our engine
engine.setProperty("voices", voices[0].id) # selecting the voice
engine.setProperty("rate", 120) #chaning the rate

# function for audio output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function that wishes you depending on wht time is it
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("GooD Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your jarvis AI How may I help you")

# function to capture the command
def takecommand():
    r=sr.Recognizer() # sr object to access it faster
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold= 1 # how long there should be the pause before capturing the command
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in') #google api to catpture the command
        print("You said: %s" %query)
        print("\n")
    except Exception as e:
        print(e)
        print("please repeat the command again")
        return "None"
    return query

if __name__ == "__main__":
    wishme() #call the function
    while True:
     query = takecommand().lower()
     # add which ever condition to make the AI more efficinet
     if 'jarvis' in query:
         speak("Yes boss")
     w =  webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
     if 'wikipedia' in query:
         speak('Searching wikipedia...')
         query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)#sentences is no of sentences that should be fetched from wikipedia
         speak("According to Wikipedia")
         speak(results)
     elif 'open youtube' in query:
        w.open("youtube.com")
     elif 'open google' in query:
         w.open("google.com")
     elif 'the time' in query:
         strtime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"The time is {strtime}")

