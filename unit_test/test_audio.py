import pyttsx3  # text to speech
import speech_recognition as sr  # speech to text

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config

engine = pyttsx3.init()  # Initiate the text to speech engine


def audio2text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Time over, thanks")
    try:
        text = r.recognize_google(audio, language="en-US")
        print("You said: " + text)
        return text
    except:
        print("Sorry could not recognize what you said")


def text2audio(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    client = GPTClient(**client_config)
    prompt_instance = PromptProcess("ielts")
    while True:
        text = audio2text()
        prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=[f"{text}"], actor_id="0")
        result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
        print("GPT-3 said: " + result[0])
        text2audio(result[0])
