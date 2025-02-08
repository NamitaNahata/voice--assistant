import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Capture and recognize speech from the microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("There was an issue with the speech recognition service.")
        except Exception as e:
            speak("Something went wrong.")
            print(f"Error: {e}")
    return ""

def get_time():
    """Get the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def get_date():
    """Get the current date"""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_wikipedia(query):
    """Search Wikipedia for a given query"""
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia: {result}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia about that.")

def open_website(query):
    """Open a website in the browser"""
    if "google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "wikipedia" in query:
        webbrowser.open("https://www.wikipedia.org")
        speak("Opening Wikipedia")
    else:
        speak("I can only open Google, YouTube, or Wikipedia.")

def main():
    """Main function to run the voice assistant"""
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = recognize_speech()

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "time" in command:
            get_time()
        elif "date" in command:
            get_date()
        elif "search wikipedia for" in command:
            query = command.replace("search wikipedia for", "").strip()
            search_wikipedia(query)
        elif "open" in command:
            query = command.replace("open", "").strip()
            open_website(query)
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
