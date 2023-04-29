from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


def client_test() -> None:
    """
    This function is responsible for testing the GPTClient class.
    """
    client = GPTClient(**client_config)
    prompt_instance = PromptProcess("gpt")
    prompt = prompt_instance.generate_model_prompt(msg="可以介绍一下自己吗", chat_history=[])
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    print(result)


if __name__ == "__main__":
    client_test()
