# Activar el entorno virtual    .venv/Scripts/activate
# pip install SpeechRecognition keyboard pyaudio
# pip install openai-whisper
""" 
import os
import tempfile
import speech_recognition as sr
from pydub import AudioSegment

# ==============================
# Configuration
# ==============================

input_file = "audio1.mp3"          # MP3 file
output_file = "transcription.txt" # Output text file
language = "en-US"                # English

# ==============================
# Convert MP3 to temporary WAV
# ==============================

print("Converting MP3 to WAV...")

audio = AudioSegment.from_mp3(input_file)

with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp:
    temp_wav = temp.name

audio.export(temp_wav, format="wav")

# ==============================
# Speech Recognition
# ==============================

recognizer = sr.Recognizer()
full_transcription = ""

try:
    with sr.AudioFile(temp_wav) as source:

        duration = int(source.FRAME_COUNT / source.SAMPLE_RATE)

        print("Processing audio...\n")

        for i in range(0, duration, 10):

            audio_chunk = recognizer.record(source, duration=10)

            if len(audio_chunk.frame_data) == 0:
                break

            try:
                text = recognizer.recognize_google(
                    audio_chunk,
                    language=language
                )

                print(f"Chunk {i//10 + 1}: {text}")

                full_transcription += text + "\n"

            except sr.UnknownValueError:
                print(f"Chunk {i//10 + 1}: Could not understand audio")
                full_transcription += "[Unrecognized]\n"

            except sr.RequestError as e:
                print(f"Google API Error: {e}")
                break

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_transcription)

    print("\nDone!")
    print(f"Saved as: {output_file}")

except Exception as e:
    print(e)

finally:
    if os.path.exists(temp_wav):
        os.remove(temp_wav)

"""
# 1) FFmpeg (necesario para Whisper) FFmpeg builds for Windows (gyan.dev)
# pip install openai-whisper

import whisper

# ==============================
# Configuration
# ==============================

input_file = "audio.mp3"
output_file = "transcription.txt"

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Transcribing...")

result = model.transcribe(
    input_file,
    language="en"   # Remove this line for automatic language detection
)

text = result["text"]

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("\nDone!")
print(text)