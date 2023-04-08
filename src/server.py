import uuid
import logging
from flask_cors import CORS
from typing import Any, List, Dict
from flask import Flask, request, jsonify

from src.GPTClient import GPTClient
from src.prompts.prompt import PromptProcess
from src.configs.configs import client_config
from src.utils.fengkong_utils import post_process_text
from src.utils.role_utils import role2actorid, actorid2role
from src.history.history_buffer import HistoryBuffer, history_buffer_add


logging.basicConfig(level=logging.INFO)


class TalkServer(object):
    """
    This TalkServer class is used to receive the request from the client and return the response.
    """

    def __init__(self) -> None:
        self.client = GPTClient(**client_config)
        roles = list(role2actorid.keys())
        self.prompt_model_dict = {role: PromptProcess(role, search_num=3) for role in roles}
        self.history_buffer = HistoryBuffer()
        server = Flask(__name__)
        CORS(server, resources=r"/*")
        server.config["JSON_AS_ASCII"] = False
        server.route("/api/chat/new", methods=["POST"])(self.new)
        server.route("/api/chat/choose", methods=["POST"])(self.choose)
        server.route("/api/chat/message", methods=["POST"])(self.message)
        server.run(host="0.0.0.0", port=8080, threaded=True)

    def new(self) -> Dict[str, Any]:
        request_data = request.get_json(force=True)
        response = {"session_id": str(uuid.uuid4())}
        return jsonify(response)

    def choose(self) -> Dict[str, Any]:
        request_data = request.get_json(force=True)
        response = {}
        return jsonify(response)

    def message(self) -> Dict[str, Any]:
        logging.info("Received message request")
        try:
            request_data = request.get_json(force=True)
            role = actorid2role[request_data["actor_id"]]
            session_id = request_data["session_id"]
            logging.debug("Request data: %s", request_data)
            # process the request and get the response
            response = self.process_request(request_data)
        except Exception as e:
            logging.error("Error processing request: %s", str(e))
            response = {"error": str(e)}

        history_buffer_add(
            history_buffer=self.history_buffer,
            role=role,
            session_id=session_id,
            query=request_data["msg"],
            response=response["msg_list"][0],
        )
        return jsonify(response)

    def process_request(self, request_data: Dict[str, Any]) -> Dict[str, List[str]]:
        msg = [request_data["msg"]]
        actor_id = request_data["actor_id"]
        session_id = request_data["session_id"]

        err = None
        for i in range(3):
            # Tips: msg can construct from self.history_buffer
            prompt = self.prompt_model_dict[actorid2role[actor_id]].generate_model_prompt(
                session_id=session_id, msg_list=msg, actor_id=actor_id
            )
            res, err = self.client.send_and_recv(
                msg=prompt,
                temp=0.9,
                out_num=1,
            )

            # 判断超过最大长度错误
            if Exception == type(err) and "context_length_exceeded" in str(err):
                return {"msg_list": ["context_length_exceeded!"]}

            if err != None or len(res) <= 0:
                continue

            # success, _ = text_verification(session_id, res[0])  # 添加风控规则
            success = True
            if success:
                # 如果返回结果为True，调用PostProcessText函数进行后处理
                new_res = post_process_text(res[0])  # 添加后处理规则
                return {"msg_list": [new_res]}
            else:
                return {"msg_list": ["这个问题我不知道呢，换个问题吧!"]}
        return {"msg_list": ["这个问题我不知道呢，换个问题吧~"]}


if __name__ == "__main__":
    TalkServer()
