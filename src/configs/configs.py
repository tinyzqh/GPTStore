import os
import platform
flags = {    
    "USE_eleven_labs":False,
    "USE_gTTS":True,
    "USE_ttsx3":False,}
# print(flags["USE_eleven_labs"])
client_config = {
    "model": "gpt-3.5-turbo",
    # "api_key": "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",
    "api_key":"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",
    "max_tokens": 500,
    "elevenlabs_key":"68aba081181042669339023720a395a4",
    "FLAG":flags,
    "use_vosk":True
    }

# def set_flag_true(flag_name,flags):
#     for key in flags:
#         flags[key] = False
#     flags[flag_name] = True

class model_config:
    if platform.system().lower() == "windows":
        # text2vec_model_path = r"D:\ccx\.cache\torch\sentence_treansformers\shibing624_text2vec-base-chinese"
        text2vec_model_path = r"C:\Users\tinyzqh\.cache\torch\sentence_transformers\shibing624_text2vec-base-chinese"
        if not os.path.exists(text2vec_model_path):
            text2vec_model_path = "shibing624/text2vec-base-chinese"
    else:
        raise Exception("Unknown system type!")

class method_config:
    use_semantic_search = False