import pandas as pd
from typing import Any, List, Dict
from src.utils.file_utils import read_text_file
from src.utils.vector_utils import sentence_embedding
from src.utils.vector_utils import retrieve_related_documents
from src.prompts.base.base_prompt import BasePromptProcess


class PromptProcess(BasePromptProcess):
    def __init__(self, role_name: str, search_num: int = 2) -> None:
        super().__init__(role_name, search_num)

    def generate_model_prompt(self, session_id: str, msg_list: List[str], actor_id: str) -> List[Dict[str, Any]]:
        """
        This function is used to generate the prompt for the model.
        
        Args:
            session_id (str): Session ID.
            msg_list (List[str]): List of messages.
            actor_id (str): Actor ID.

        Returns:
            List[Dict[str, Any]]: List of prompts.
        """
        assert isinstance(msg_list, list), "msg_list must be a list."
        prompt = []

        # 1. system-background
        system_info = {"role": "system", "content": read_text_file(self.system_file_path)}
        prompt.append(system_info)

        # 2. knowledge
        query = msg_list[-1]
        knowledges = self.search(query)
        part_facts = read_text_file(self.facts_describe_path) + "".join(knowledges)

        user_info = {"role": "user", "content": part_facts}
        prompt.append(user_info)

        # query
        prompt.append({"role": "user", "content": read_text_file(self.user_file_path) + "Q:" + query + "\nA:"})

        # 3. assistant
        prompt.append({"role": "assistant", "content": read_text_file(self.assistant_file_path) + "\nA:"})
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

    
    