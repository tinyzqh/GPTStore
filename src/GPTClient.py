import os
import openai
from typing import Any, List, Dict, Tuple


class GPTClient:
    def __init__(self, model: str, api_key: str, max_tokens: int,elevenlabs_key:str,FLAG:Dict,use_vosk:bool) -> None:
        self.model = model
        self.api_key = api_key
        self.max_tokens = max_tokens
        self.elevenlabs_key=elevenlabs_key
        openai.api_key = self.api_key
        self.flags=FLAG
        self.use_vosk=use_vosk
    def send_and_recv(self, msg: List[Dict[str, Any]], temp: float, out_num: int) -> Tuple[List[str], Exception]:
        self.set_proxy()
        respond = openai.ChatCompletion.create(
            model=self.model,
            messages=msg,
            max_tokens=self.max_tokens,
            temperature=temp,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0,
            # stop=["\n", " Human:", " AI:"],
        )
        self.unset_proxy()
        result = [respond.choices[0].message["content"]]
        err = None
        return result, err

    def set_proxy(self) -> None:
        os.environ["https_proxy"] = "http://127.0.0.1:7890"
        os.environ["http_proxy"] = "http://127.0.0.1:7890"

    def unset_proxy(self) -> None:
        os.environ["https_proxy"] = ""
        os.environ["http_proxy"] = ""
