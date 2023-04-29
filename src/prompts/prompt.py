import pandas as pd
from typing import Any, List, Dict
from src.utils.file_utils import read_text_file
from src.utils.vector_utils import sentence_embedding
from src.utils.vector_utils import retrieve_related_documents
from src.prompts.base.base_prompt import BasePromptProcess


class PromptProcess(BasePromptProcess):
    def __init__(self, role_name: str, search_num: int = 2) -> None:
        super().__init__(role_name, search_num)

    def generate_model_prompt(self, msg: str, chat_history: List[str]) -> List[Dict[str, Any]]:
        """
        This function is used to generate the prompt for the model.
        
        Args:
            msg (str): str of messages.
            chat_history (List[str]): List of chat history.

        Returns:
            List[Dict[str, Any]]: List of prompts.
        """
        assert isinstance(msg, str), "msg must be str."
        prompt = []

        # 1. system-background
        system_info = {"role": "system", "content": read_text_file(self.system_file_path)}
        prompt.append(system_info)

        # 2. knowledge
        query = msg
        knowledges = self.search(query) if self.use_semantic_search else ""
        part_facts = read_text_file(self.facts_describe_path) + "".join(knowledges)
        
        

        user_info = {"role": "user", "content": part_facts}
        prompt.append(user_info)
        

        # query
        prompt.append({"role": "user", "content": read_text_file(self.user_file_path) + "Q:" + query + "\nA:"})

        # 3. assistant
        if len(chat_history) > 0:
            history = "The conversation was recorded as: " + ";".join([f"human: {chat[0]}; bot: {chat[1]}" for chat in chat_history])
        else:
            history = ""
            
        prompt.append({"role": "assistant", "content": history + "\n" + read_text_file(self.assistant_file_path) + "\nA:"})
        return prompt

    def search(self, query: str) -> List[str]:
        """
        This function is used to search the knowledge base for the top k most relevant documents to the query.

        Args:
            query (str): Query.
        
        Returns:
            List[str]: List of knowledge.
        """
        query_emb = sentence_embedding(self.text2vec_model, query)
        df_knowledge = pd.read_csv(self.index_path, encoding="utf-8")
        knowledge_score_pairs = retrieve_related_documents(query_emb, df_knowledge)
        return [knowledge[0] for knowledge in knowledge_score_pairs[: self.search_num]]

    
    