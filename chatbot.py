import sys
import pyaudio
import wave
import whisper
import cohere
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# CONFIG
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5  # duration of the audio input to analyze
WAVE_OUTPUT_FILENAME = "temp_input.wav"

# COHERE API KEY HERE
COHERE_API_KEY = "COHERE_API_KEY_HERE"


sys.stdout.reconfigure(encoding='utf-8')    # To accept Arabic characters in the console


# SETUP
audio = pyaudio.PyAudio()
whisper_model = whisper.load_model("base")
co = cohere.Client(COHERE_API_KEY)

def record_audio():
    print("Listening...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path, language="ar")
    return result["text"]

def generate_response(prompt):
    response = co.chat(
        message=prompt,
        model="command-r7b-arabic-02-2025",
        temperature=0.5,
    )
    return response.text.strip()

def speak_text(text, filename="response.mp3"):
    tts = gTTS(text=text, lang='ar')
    tts.save(filename)
    audio_segment = AudioSegment.from_mp3(filename)
    play(audio_segment)
    os.remove(filename)

# MAIN LOOP
def main():
    print("Arabic Voice Assistant is running (Ctrl+C to stop)...")
    try:
        while True:
            record_audio()
            text = transcribe_audio(WAVE_OUTPUT_FILENAME)
            print("You said:", text)

            if text.strip() == "":
                print("No speech detected.")
                continue

            response = generate_response(text)
            print("Bot:", response)
            speak_text(response)

    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        audio.terminate()
        if os.path.exists(WAVE_OUTPUT_FILENAME):
            os.remove(WAVE_OUTPUT_FILENAME)

if __name__ == "__main__":
    main()
