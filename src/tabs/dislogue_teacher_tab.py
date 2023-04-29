import random
import gradio as gr


from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_instance = PromptProcess("ielts_dialogue")


def respond(message, chat_history):
    prompt = prompt_instance.generate_model_prompt(msg=message, chat_history=chat_history[-5:])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_message = result[0]
    chat_history.append((message, bot_message))
    return "", chat_history


def DialogueTeacherTab():
    with gr.Tab("IELTS Dialogue Teacher"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="Input:")
        gr.Examples(
            examples=["who are you?", "What I just said?", "What do you think about artificial intelligence?"],
            inputs=[msg],
        )
        clear = gr.Button("Clear")

        msg.submit(respond, [msg, chatbot], [msg, chatbot], queue=False)
        clear.click(lambda: None, None, chatbot, queue=False)
