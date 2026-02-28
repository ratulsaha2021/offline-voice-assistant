# Offline Voice Assistant Prototype

A privacy-focused, 100% offline voice assistant that uses Speech-to-Text (STT), a local knowledge base (RAG), and Text-to-Speech (TTS).


## ✨ Features
- **Offline STT:** Powered by Vosk for local speech recognition.
- **Hybrid Intelligence:** Uses rule-based logic for common queries (time, date) and TF-IDF Retrieval-Augmented Generation (RAG) for facts.
- **Offline TTS:** Uses `pyttsx3` for immediate voice feedback.
- **Custom Knowledge:** Easily expandable via `knowledge.txt`.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/offline-voice-assistant.git](https://github.com/yourusername/offline-voice-assistant.git)
   cd offline-voice-assistant
