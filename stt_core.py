import json

import numpy as np
import sounddevice as sd
from vosk import Model, KaldiRecognizer


# 1. Load the Vosk model from disk (adjust path)
MODEL_PATH = rMODEL_PATH = r"C:\Users\Ratul Saha\Downloads\vosk-model-small-en-us-0.15"
  # change if needed

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)  # 16 kHz sample rate[web:59][web:90]


def listen_once() -> str:
    """
    Record from microphone until Vosk thinks a full sentence is done,
    then return the recognized text.
    """
    print("Speak now...")
    with sd.InputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
    ) as stream:
        while True:
            data, _ = stream.read(4000)   # data is a NumPy array
            # Convert NumPy array to bytes for Vosk
            data_bytes = data.tobytes()

            if recognizer.AcceptWaveform(data_bytes):
                result_json = recognizer.Result()
                result = json.loads(result_json)
                text = result.get("text", "")
                print("Heard:", text)
                return text

if __name__ == "__main__":
    while True:
        text = listen_once()
        if not text:
            continue
        if "stop" in text.lower():
            print("Stopping.")
            break
