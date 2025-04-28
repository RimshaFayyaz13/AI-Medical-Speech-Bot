import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO 
import os
from groq import Groq


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'  # <- this is the correct key
)
def record_audio(file_path, timeout=100, phrase_time_limit=100):
    """
    Records audio from the microphone and saves it to a file as mp3.

    Arg:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for speech input (in seconds).
    phrase_time_limit (int): Maximum time to record a single phrase (in seconds).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            #setting ambient noise adjustment for 1 sec
            logging.info("adjustments for clear voices...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start Speaking now...")
            
            #record and convert the audio file into an MP3 file
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording finished.")

            #now converting the record audio to an  mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occured: {e}")

audio_filepath = "patient_voice_test.mp3"
record_audio(file_path=audio_filepath)

#STEP 2: Speech to text-SST-model fro transcribing the audio file
stt_model="whisper-large-v3-turbo"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def transcribe_with_groq(audio_filepath, stt_model, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en",
        
    )
    return transcription.text