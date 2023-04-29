import gradio as gr

from src.tabs.gpt_tab import ChatGptTab
from src.tabs.dislogue_teacher_tab import DialogueTeacherTab
from src.tabs.writing_teacher_tab import WritingTeacherTab
from src.tabs.translation_tab import TranslationTab


with gr.Blocks() as demo:
    gr.Markdown("GPT个人助手")
    ChatGptTab()
    TranslationTab()
    DialogueTeacherTab()
    WritingTeacherTab()


if __name__ == "__main__":
    demo.launch(share=True)  # auth=(["123", "123"])
