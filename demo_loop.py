from voice_core import speak
from stt_core import listen_once

def main():
    while True:
        text = listen_once()
        if not text:
            continue
        print("you said:", text)

        if "stop" in text.lower():
            print("Goodbye")
            break

        speak("You said: " + text)

    

if __name__ == "__main__":
    main()


