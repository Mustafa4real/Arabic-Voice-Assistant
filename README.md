# Arabic-Voice-Assistant

In this project I developed an Arabic-speaking voice assistant that listens to your voice, transcribes your Arabic speech using OpenAI's **Whisper**, generates smart responses using Cohere's **command-r7b-arabic-02-2025** LLM, and replies to you using speech via **Google Text-to-Speech** and **PyDub**.

## Features

- Real-time voice recording and transcription (Arabic)
- Context-aware text generation using Cohere's Arabic language model
- Spoken responses using gTTS
- Fully automated conversational loop

## Tech Stack

- [_**OpenAI Whisper**_] for speech-to-text
- [_**Cohere**_] for Arabic LLM-based response generation
- [_**gTTS**_] for text-to-speech in Arabic
- [_**PyAudio**_] for microphone input
- [_**PyDub**_] for audio playback

## How to run
1. Install dependencies: `pip install -r requirements.txt`.
2. Download FFmpeg: https://ffmpeg.org/.
3. Replace _"COHERE_API_KEY_HERE"_ in `chatbot.py` with your actual API Key.
4. Run `chatbot.py`.

## Demo


https://github.com/user-attachments/assets/a0d39564-6508-4da5-bfed-098658519197

