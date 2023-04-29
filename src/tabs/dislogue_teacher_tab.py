import random
import gradio as gr


from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


client = GPTClient(**client_config)
prompt_obj = PromptProcess("ielts_dialogue")


def generate_bot_response(message, chat_history):
    """
    Generates a response from the chatbot model based on the input message and chat history.

    Args:
    message (str): The user's message input.
    chat_history (List[Tuple[str, str]]): A list of tuples containing the conversation history.

    Returns:
    A tuple containing the generated bot response and updated chat history.
    """
    prompt = prompt_obj.generate_model_prompt(
        msg=message, chat_history=chat_history[-5:]
    )
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    bot_msg = result[0]
    chat_history.append((message, bot_msg))
    return "", chat_history


def DialogueTeacherTab():
    """
    Defines the IELTS Dialogue Teacher tab for the Gradio web app.
    """
    with gr.Tab("IELTS Dialogue Teacher"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="Input:")
        gr.Examples(
            examples=[
                "who are you?",
                "What I just said?",
                "What do you think about artificial intelligence?",
            ],
            inputs=[msg],
        )
        clear = gr.Button("Clear")

        # when submit button is clicked, call the generate_bot_response function with the message input and chat history
        msg.submit(generate_bot_response, [msg, chatbot], [msg, chatbot], queue=False)

        # when clear button is clicked, empty the chat history
        clear.click(lambda: None, None, chatbot, queue=False)
