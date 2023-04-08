from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config


def client_test() -> None:
    """
    This function is responsible for testing the GPTClient class.
    """
    client = GPTClient(**client_config)
    prompt_instance = PromptProcess("ielts")
    prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=["可以简要介绍一下你自己吗？"], actor_id="0")
    result, err = client.send_and_recv(msg=prompt, temp=0.9, out_num=1)
    print(result)


if __name__ == "__main__":
    client_test()
