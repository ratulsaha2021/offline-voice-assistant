import pyttsx3
engine= pyttsx3.init()

def speak(text: str):
    """Say a text string a loud."""
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak("Raiyan motherfucker")
