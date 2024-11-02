import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice assistant's properties
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice command."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return ""
        
    return command

def greet():
    """Greet the user."""
    speak("Hello! How can I assist you today?")

def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    """Tell today's date."""
    today_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today_date}")

def search_web(query):
    """Search the web for a given query."""
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main loop for the voice assistant
def voice_assistant():
    speak("Starting voice assistant.")
    while True:
        command = listen()
        
        if 'hello' in command:
            greet()
        
        elif 'time' in command:
            tell_time()
        
        elif 'date' in command:
            tell_date()
        
        elif 'search' in command:
            speak("What would you like to search for?")
            query = listen()
            if query:
                search_web(query)
        
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    voice_assistant()
