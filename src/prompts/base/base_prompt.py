import os
from typing import Any, List, Dict
from src.configs.configs import model_config
from sentence_transformers import SentenceTransformer
from src.configs.configs import model_config, method_config
from src.utils.vector_utils import generate_knowledge_index


class BasePromptProcess:
    """
    Base class for generating GPT prompt.

    Attributes:
        role_name (str): Name of the role.
        parent_dir (str): Absolute path of the parent directory.
        role_path (str): Absolute path of the role directory.
        system_file_path (str): Absolute path of the system background file.
        user_file_path (str): Absolute path of the user file.
        knowledges_path (str): Absolute path of the knowledge base file.
        index_path (str): Absolute path of the knowledge index file.
        facts_describe_path (str): Absolute path of the facts describe file.
        assistant_file_path (str): Absolute path of the assistant file.
        text2vec_model (SentenceTransformer): SentenceTransformer model.
        search_num (int): Number of search results.
    """

    def __init__(self, role_name: str, search_num: int = 2) -> None:
        """
        Initialize the BasePromptProcess class.

        Args:
            role_name (str): Name of the role.
            search_num (int): Number of search results.

        Returns:
            None
        """
        self.role_name: str = role_name
        self.parent_dir: str = os.path.abspath(os.path.join(os.getcwd(), "."))
        self.role_path: str = f"{self.parent_dir}/src/corpus/{self.role_name}"
        self.system_file_path: str = f"{self.role_path}/system.txt"
        self.user_file_path: str = f"{self.role_path}/user.txt"
        self.knowledges_path: str = f"{self.role_path}/knowledges.txt"
        self.facts_describe_path: str = f"{self.role_path}/facts_describe.txt"
        self.assistant_file_path: str = f"{self.role_path}/assistant.txt"
        self.index_path = f"{self.role_path}/knowledge_embeddings.csv"
        
        self.use_semantic_search = method_config.use_semantic_search
        if self.use_semantic_search:
            self.text2vec_model = SentenceTransformer(model_config.text2vec_model_path, device="cpu")
            generate_knowledge_index(self.text2vec_model, self.knowledges_path)
            self.search_num = search_num
        

    def generate_model_prompt(self, session_id: str, msg_list: List[str], actor_id: str) -> List[Dict[str, Any]]:
        """
        Generate model prompt.

        Args:
            session_id (str): Session ID.
            msg_list (List[str]): List of messages.
            actor_id (str): Actor ID.

        Returns:
            List[Dict[str, Any]]: List of prompts.
        """
        pass

    def search(self, query: str) -> List[str]:
        """
        Searches the knowledge base for the top k most relevant documents to the query.

        Args:
            query (str): The search query.

        Returns:
            List[str]: A list of the top k most relevant documents.
        """
        pass
