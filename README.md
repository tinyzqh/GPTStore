# TalkBotGPT

TalkBotGPT 是一个基于 ChatGPT 的对话式个人助手项目。它利用了 OpenAI 的 GPT-3.5 模型作为核心引擎，为用户提供先进的自然语言处理能力。TalkBotGPT 可以应用于多种场景，包括在线雅思对话老师、雅思写作润色老师、翻译软件、社交聊天等。

仅修改不到30行代码即可构建自己的个人助手，如论文阅读助手，面试考官助手，周报总结助手，文字游戏休闲助手，吃饭推荐助手，安慰女朋友话术助手等等。

## Features

- 轻量级: 界面采用gradio搭建，轻量级，易于使用。
- 支持自定义智能体：轻松构建自己工作中常用的工具，只需要改一点Prompt即可。
- 支持语义检索本地文档：轻松构建自己的本地知识库。
- 支持在线检索：基于bing搜索引擎的搜索结果，给到GPT做后续处理。
- 支持语音输入：轻松构建自己的语音输入工具，相关文件在unit_test/test_audio.py。
- 灵活的接口：TalkBotGPT 提供简单易用的接口，可以与其他应用或服务无缝集成，实现对话功能的可扩展性和定制性。

## Interface Display

TalkBotGPT 是一个功能强大的对话式聊天机器人项目，为开发者和用户提供丰富的对话生成能力，帮助他们构建智能、灵活、可定制的对话应用。无论是用于商业应用还是个人项目，TalkBotGPT 都可以为用户带来便利和创新。以下是一些基础功能，开发者可以基于此进行快速的二次开发。

### 原始GPT

<div align="center">
<img src="https://github.com/tinyzqh/TalkBotGPT/blob/main/pic/gpt.jpeg" width="800" >
</div>

### 翻译

<div align="center">
<img src="https://github.com/tinyzqh/TalkBotGPT/blob/main/pic/translate.jpeg" width="800" >
</div>

### 雅思对话老师

<div align="center">
<img src="https://github.com/tinyzqh/TalkBotGPT/blob/main/pic/ielts_dialogue.jpeg" width="800" >
</div>

### 雅思写作修改老师

<div align="center">
<img src="https://github.com/tinyzqh/TalkBotGPT/blob/main/pic/ielts_write.jpeg" width="800" >
</div>

## Getting Started

要开始使用 TalkBotGPT，请按照以下步骤操作:

1. 将本仓库克隆到您的本地机器。
2. 按照文档中的说明安装所需的依赖项。

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

3. 在 src/config.py 中用您自己的 api_key 替换原有的 api_key。
3. 运行演示程序或使用提供的示例与 TalkBotGPT 进行互动。

```bash
cd TalkBotGPT
export PYTHONPATH=.  # set PYTHONPATH
python src/local_ui_session.py  # test local ui session
```

4. 根据您的需求定制 TalkBotGPT，并将其集成到您的项目中。

有关详细的使用说明和示例，请参阅[文档](https://github.com/tinyzqh/TalkBotGPT/wiki).


## 如何添加自己的个人助手？

1. 仓库中local_ui_session.py是启动脚本，每次添加一个个人助手，只需要在tabs里面新建一个.py文件，基于gradio构建一个新的tab即可在local_ui_session.py中导入即可。
2. tabs里的.py文件，需要构建对话处理逻辑。其中需要修改prompt，因此需要在src/corpus里面构建一个智能体的设定, 之后prompt会读取这个智能体的设定，然后根据用户输入的内容，构建prompt，然后将prompt输入到GPT中，得到回复。如果你的prompt构建与给定的prompt构建框架不一致，你也可以参考目前的prompt构建框架，自己构建一个prompt构建框架。


## TODO

1. 修改prompt，使得对话更加流畅。
2. 添加历史对话总结功能。(参考langchain)
3. 对代码添加注释，方便阅读。
4. 添加更多的智能体，比如论文阅读助手，面试考官助手，周报总结助手，文字游戏休闲助手，吃饭推荐助手，安慰女朋友话术助手等等。


## Contributing
我们欢迎社区的贡献！如果您想为 TalkBotGPT 做贡献，请查阅[贡献指南](CONTRIBUTING.md)以获取详细信息和开始的方法。


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=tinyzqh/TalkBotGPT&type=Date)](https://star-history.com/#tinyzqh/TalkBotGPT&Date)

## License
TalkBotGPT 是一款开源软件，根据[MIT License](LICENSE)进行许可。请根据许可证的条款自由使用、修改和分发。

## Contact Us

如果您有任何问题、建议或反馈，请随时[联系我们](mailto:tinyzqh@163.com)。我们欢迎您的意见，并乐意协助解答任何疑问。谢谢您的支持！