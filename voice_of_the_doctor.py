import os
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from elevenlabs import save
import subprocess
import platform
from pydub import AudioSegment  

# def convert_mp3_to_wav(output_file_path, wav_path):
#     sound = AudioSegment.from_mp3(output_file_path)
#     sound.export(wav_path, format="wav")

# #Step 1: Text to Speech using gTTS
# def text_to_speech_with_gtts_old(input_text, output_file_path):
#     language = 'en'
#     audioobj = gTTS(
#         text=input_text, 
#         lang=language, 
#         slow=False)
#     audioobj.save(output_file_path)
    

# input_text = "Hello, how can I assist you today?"
#text_to_speech_with_gtts_old(input_text=input_text, output_file_path="testing_gTTS.mp3")

#Step 2: Text to Speech-TTS using ElevenLabs
load_dotenv()
ElevenLabs_API_KEY = os.getenv("ElevenLabs_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_file_path):
#     client = ElevenLabs(api_key=ElevenLabs_API_KEY)
#     # Generate audio as a stream (generator)
#     audio=client.generate(
#         text=input_text,
#         voice="Aria",  # You can change this to a valid voice name you have access to
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2"
#     )
#     save(audio,output_file_path)
#     # pass
# input_text1="Hello, how can I help you today?"   
#text_to_speech_with_elevenlabs_old(input_text1, output_file_path="elevenlabs_test.mp3")

#Step 3: Use Model for Text output to voice
def text_to_speech_with_gtts(input_text, output_file_path):
    language = 'en'
    audioobj = gTTS(
        text=input_text, 
        lang=language, 
        slow=False)
    audioobj.save(output_file_path)
        # Convert to wav for playback
    sound = AudioSegment.from_mp3(output_file_path)
    sound.export(output_file_path, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_file_path}" ).PlaySync();'])
        else:
            raise OSError("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")
input_text = "Hello, I am testing gTTS auto play for doctor bot?"
# text_to_speech_with_gtts(input_text=input_text, output_file_path="testing_gTTS_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_file_path):
    client = ElevenLabs(api_key=ElevenLabs_API_KEY)
    # Generate audio as a stream (generator)
    audio_stream=client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",  # You can change this to a valid voice name you have access to
        output_format="mp3_22050_32",
        model_id="eleven_multilingual_v1"
    )

    with open(output_file_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    sound = AudioSegment.from_mp3(output_file_path)
    sound.export(output_file_path, format="wav")

    os_name = platform.system()

    # wav_path1 = output_file_path.replace(".mp3", ".wav")
    # convert_mp3_to_wav(output_file_path, wav_path1)
    # os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_file_path}" ).PlaySync();'])
        else:   
            raise OSError("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")
    print(f"Audio saved to: {output_file_path}")
    # pass
# input_text1="Hello, I am AI doctor from ElevenLabs?"   
# text_to_speech_with_elevenlabs(input_text1, output_file_path="elevenlabs_test_autoplay.mp3")

    # # Save the stream manually
    # with open(output_file_path, "wb") as f:
    #     for chunk in audio_stream:
    #         f.write(chunk)

