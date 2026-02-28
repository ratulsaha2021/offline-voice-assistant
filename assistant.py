from voice_core import speak
from stt_core import listen_once
from rag_core import rag_answer


def rule_based_answer(text: str) -> str | None:
    t = text.lower()

    if "your name" in t or "who are you" in t:
        return "I am your offline voice assistant prototype."

    if "what can you do" in t:
        return "I can listen to your voice, search in my local knowledge, and answer back with speech."

    if "date" in t and "today" in t:
        from datetime import datetime
        today = datetime.now().strftime("%d %B %Y")
        return f"Today is {today}."

    if "time" in t and "what" in t:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"The current time is {now}."

    return None


def answer_question(text: str) -> str:
    rb = rule_based_answer(text)
    if rb is not None:
        return rb
    return rag_answer(text)


def main():
    speak("Offline voice assistant started. Say something, or say stop to exit.")

    while True:
        print("Listening for your question...")
        question = listen_once()
        if not question:
            print("Heard nothing, listening again.")
            continue

        print("You said:", question)

        if "stop" in question.lower() or "exit" in question.lower():
            speak("Shutting down. Goodbye.")
            break

        answer = answer_question(question)
        print("Answer:", answer)
        speak(answer)


if __name__ == "__main__":
    main()


