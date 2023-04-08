import time
import requests
import gradio as gr
from threading import Thread
from src.server import TalkServer


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        url = "http://127.0.0.1:8080/api/chat/message"
        msg = history[-1][0]
        data = {"session_id": "1", "msg": msg, "actor_id": "1"}
        response = requests.post(url, json=data)
        bot_message = response.json()["msg_list"][0]
        # bot_message = "Hello, I am a chatbot."
        history[-1][1] = bot_message
        time.sleep(1)
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    thread = Thread(target=TalkServer)
    thread.start()

    demo.launch()
