import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Ask the user for text input
text = input("Enter the text you want to convert to speech: ")

# Convert the text to speech
engine.say(text)
engine.runAndWait()

print("Speech conversion complete!")
