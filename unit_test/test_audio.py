import pyttsx3  # text to speech
import speech_recognition as sr  # speech to text

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config
from elevenlabslib import *
import sys
import pygame
from gtts import gTTS
import tempfile
import io
import os
from vosk import Model,KaldiRecognizer
import time
t1 = time.time()
model = Model('model')
t2=time.time()
print(t2-t1)
engine = pyttsx3.init()  # Initiate the text to speech engine


# def audio2text():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
#         print("Time over, thanks")
#     try:
#         text = r.recognize_vosk(audio, language="en-US")
#         print("You said: " + text)
#         return text
#     except:
#         print("Sorry could not recognize what you said")

def audio2text(offline=True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        if offline:
            rec = KaldiRecognizer(model,16000)
            rec.AcceptWaveform(audio.get_raw_data(convert_rate=16000, convert_width=2))
        print("Time over, thanks")
    try:
        if offline:
            text = rec.FinalResult()
        else:
            text = r.recognize_google(audio, language="en-US")
        print("You said: " + text)
        return text
    except:
        print("Sorry could not recognize what you said")

def text2audio(text):
    engine.say(text)
    engine.runAndWait()
    
def text2audio_eleven(text):
    voice.generate_and_play_audio(result[0], playInBackground=False)
    for historyItem in user.get_history_items():
        if historyItem.text == "Test.":
            # The first items are the newest, so we can stop as soon as we find one.
            historyItem.delete()
  


if __name__ == "__main__":
    client = GPTClient(**client_config)
    prompt_instance = PromptProcess("ielts")
    #use elevenlabs for text to speech
    if client.flags["USE_eleven_labs"]:
        user =ElevenLabsUser(client.elevenlabs_key)
        voice = user.get_voices_by_name("Rachel")[0]
        voice.play_preview(playInBackground=True)
        while True:
            text = audio2text()
            prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=[f"{text}"], actor_id="0")
            result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
            print("GPT-3 said: " + result[0])
            voice.generate_and_play_audio(result[0], playInBackground=False)
            for historyItem in user.get_history_items():
                if historyItem.text == "Test.":
                    # The first items are the newest, so we can stop as soon as we find one.
                    historyItem.delete()
                    # break
    #use pyttsx3 for text to speech
    elif client.flags["USE_ttsx3"]:
        while True:
            text = audio2text()
            prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=[f"{text}"], actor_id="0")
            result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
            print("GPT-3 said: " + result[0])
            text2audio(result[0])
            
    elif client.flags["USE_gTTS"]:
        pygame.mixer.init()
        language = 'en'
        try:
            while True:
                text = audio2text()
                prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=[f"{text}"], actor_id="0")
                result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
                print("GPT-3 said: " + result[0])
                tts = gTTS(text=result[0], lang=language, slow=False)
                temp_audio_files = []
                with tempfile.NamedTemporaryFile(delete=True) as temp_audio_file:
                    temp_audio_file_name = f"{temp_audio_file.name}.mp3"
                    tts.save(temp_audio_file_name)

                    # Load the audio with pygame
                    pygame.mixer.music.load(temp_audio_file_name)
                    temp_audio_files.append(temp_audio_file_name)
                    # Play the audio
                    pygame.mixer.music.play()

                    # Wait for the audio to finish playing
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                        # Delete the temporary audio file   

        except KeyboardInterrupt:
            pygame.mixer.quit()
            for file_name in temp_audio_files:
                os.remove(file_name)
            temp_audio_files.clear()
            print('delete success')

    else:
        print('Please set flags in config.py')