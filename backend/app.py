from gtts import gTTS
from transformers import pipeline

# Input text
text = "Hello, this is a Google TTS demo."

# Generate speech
tts = gTTS(text, lang="en")
tts.save("outputs/output.mp3")
print("TTS complete! Output saved as 'output.mp3'.")


asr_pipeline = pipeline(model="openai/whisper-large-v2", task="automatic-speech-recognition")

def transcribe_audio(audio_path):
    transcription = asr_pipeline(audio_path)

    return transcription["text"]