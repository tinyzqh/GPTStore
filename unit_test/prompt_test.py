from src.prompts.prompt import PromptProcess


def test_english_teacher():
    prompt_instance = PromptProcess("ielts")
    prompt = prompt_instance.generate_model_prompt(session_id="0", msg_list=["可以简要介绍一下你自己吗？"], actor_id="0")
    print(prompt)


if __name__ == "__main__":
    test_english_teacher()
