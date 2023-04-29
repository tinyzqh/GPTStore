import random
import gradio as gr

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_obj = PromptProcess("gpt")


def generate_bot_response(message, chat_history):
    """
    Given a user message and chat history, generates a prompt for the GPT model and sends it to the model for
    prediction. Appends the user message and generated response to the chat history and returns the updated
    chat history.

    Args:
        message (str): The user message to respond to.
        chat_history (list): A list of tuples containing the user message and corresponding bot response for
        previous messages in the chat.

    Returns:
        tuple: A tuple containing an empty string (to satisfy the expected format of the gr.Chatbot object) and
        the updated chat history.
    """

    # Generate model prompt using user message and last 5 messages from chat history
    prompt = prompt_obj.generate_model_prompt(
        msg=message, chat_history=chat_history[-5:]
    )

    # Send prompt to GPT model and retrieve response
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_msg = result[0]

    # Append user message and generated response to chat history
    chat_history.append((message, bot_msg))

    # Return updated chat history
    return "", chat_history


def ChatGptTab():
    """
    # Define GUI tab for chatbot interface
    """
    with gr.Tab("原始GPT"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="输入:")
        gr.Examples(examples=["你是谁?", "午餐肉可以晚上吃吗？", "给我讲个笑话吧。"], inputs=[msg])
        clear = gr.Button("清除")

        # Set up message submission and clear button callbacks
        msg.submit(generate_bot_response, [msg, chatbot], [msg, chatbot], queue=False)
        clear.click(lambda: None, None, chatbot, queue=False)
