import random
import gradio as gr

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_obj = PromptProcess("ielts_write")

input_letter = []
respond_letter = []


def respond(message, chat_history):
    if len(chat_history) == 0:
        chat_history.append((input_letter[0], respond_letter[0]))
    prompt = prompt_obj.generate_model_prompt(
        msg=message, chat_history=chat_history[-5:]
    )
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_msg = result[0]
    chat_history.append((message, bot_msg))
    return "", chat_history


def submit_respond(message):
    input_letter.clear()
    respond_letter.clear()

    input_letter.append(message)
    prompt = prompt_obj.generate_model_prompt(msg=message, chat_history=[])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_msg = result[0]
    respond_letter.append(bot_msg)
    return bot_msg


def WritingTeacherTab():
    with gr.Tab("IELTS Writing Teacher"):
        with gr.Row() as row:
            with gr.Column():
                input_letter = gr.Textbox(label="Enter Essay")
                output_letter = gr.Textbox(label="Modified Essay")
                btn = gr.Button("Submit")
                gr.Examples(
                    examples=[
                        "The bar chart compares the amount of time spent by people in the UK on three different types of phone call between 1995 and 2002. \
                        It is clear that calls made via local, fixed lines were the most popular type, in terms of overall usage, throughout the period shown.\
                        The lowest figures on the chart are for mobile calls, but this category also saw the most dramatic increase in user minutes.\
                        In 1995, people in the UK used fixed lines for a total of just over 70 billion minutes for local calls, and about half of that amount of time for national or international calls.\
                        By contrast, mobile phones were only used for around 4 billion minutes. Over the following four years, the figures for all three types of phone call increased steadily.\
                        By 1999, the amount of time spent on local calls using landlines had reached a peak at 90 billion minutes. Subsequently, the figure for this category fell, but the rise in the other two types of phone call continued.\
                        In 2002, the number of minutes of national / international landline calls passed 60 billion, while the figure for mobiles rose to around 45 billion minutes."
                    ],
                    inputs=[input_letter],
                )
                btn.click(
                    fn=submit_respond, inputs=[input_letter], outputs=output_letter
                )

            with gr.Column():
                chatbot = gr.Chatbot(label="ChatGPT")
                msg = gr.Textbox(label="Question")
                clear = gr.Button("Clear")

                msg.submit(respond, [msg, chatbot], [msg, chatbot], queue=False)
                clear.click(lambda: None, None, chatbot, queue=False)
