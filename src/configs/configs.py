import platform

client_config = {
    "model": "gpt-3.5-turbo",
    "api_key": "sk-xx",
    "max_tokens": 500,
}


class model_config:
    if platform.system().lower() == "windows":
        text2vec_model_path = r"C:\Users\tinyzqh\.cache\torch\sentence_transformers\shibing624_text2vec-base-chinese"
    else:
        raise Exception("Unknown system type!")
