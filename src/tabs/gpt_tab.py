import random
import gradio as gr

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_instance = PromptProcess("gpt")


def respond(message, chat_history):
    prompt = prompt_instance.generate_model_prompt(msg=message, chat_history=chat_history[-5:])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_message = result[0]
    chat_history.append((message, bot_message))
    return "", chat_history


def ChatGptTab():
    with gr.Tab("原始GPT"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="输入:")
        gr.Examples(examples=["你是谁?", "午餐肉可以晚上吃吗？", "给我讲个笑话吧。"], inputs=[msg])
        clear = gr.Button("清除")

        msg.submit(respond, [msg, chatbot], [msg, chatbot], queue=False)
        clear.click(lambda: None, None, chatbot, queue=False)
