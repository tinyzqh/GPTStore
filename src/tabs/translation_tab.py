import random
import gradio as gr

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_instance = PromptProcess("ielts_translate")

messages = []
responds = []


def translate(message, language_change):
    message = "please translate this sentence into " + language_change + ": " + message + "\n"
    prompt = prompt_instance.generate_model_prompt(msg=message, chat_history=[])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_message = result[0]
    messages.append(message)
    responds.append(bot_message)
    return bot_message


def respond(message, chat_history):
    if len(chat_history) == 0:
        chat_history.append((messages[0], responds[0]))
    prompt = prompt_instance.generate_model_prompt(msg=message, chat_history=chat_history[-5:])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_message = result[0]
    chat_history.append((message, bot_message))
    return "", chat_history


def TranslationTab():
    with gr.Tab("翻译"):
        with gr.Row() as row:
            with gr.Column():
                input_letter = gr.Textbox(label="输入:")

                language_change_btn = gr.Radio(["English", "Japanese", "Chinese"], label="翻译语言")
                #
                language_change_btn.change(fn=lambda x: x, inputs=language_change_btn, outputs=language_change_btn)

                submit_btn = gr.Button("提交")
                examples = gr.Examples(
                    examples=["I went to the supermarket yesterday.", "我昨天去了超市。"], inputs=[input_letter]
                )

                output_letter = gr.Textbox(label="翻译结果输出:")

                submit_btn.click(
                    translate,
                    inputs=[input_letter, language_change_btn],
                    outputs=output_letter,
                    api_name="translate-to-german",
                )

            with gr.Column():
                chatbot = gr.Chatbot(label="会话记录")
                msg = gr.Textbox(label="问题输入:")
                clear = gr.Button("Clear")

            msg.submit(respond, [msg, chatbot], [msg, chatbot], queue=False)
            clear.click(lambda: None, None, chatbot, queue=False)
