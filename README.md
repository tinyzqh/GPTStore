# TalkBotGPT

TalkBotGPT 是一个基于 ChatGPT 的对话式个人助手项目。它利用了 OpenAI 的 GPT-3.5 模型作为核心引擎，为用户提供先进的自然语言处理能力。TalkBotGPT 可以应用于多种场景，包括在线雅思对话老师、雅思写作润色老师、翻译软件、社交聊天等。

<div align="center">
<img src="https://github.com/tinyzqh/TalkBotGPT/blob/main/pic/chat.png" width="700" >
</div>

## Features

- 支持自定义智能体：轻松构建自己工作中常用的工具，只需要改一点Prompt即可。
- 支持语义检索本地文档：轻松构建自己的本地知识库。
- 支持语音输入：轻松构建自己的语音输入工具。
- 支持在线检索：基于bing搜索引擎的搜索结果，给到GPT做后续处理。
- 灵活的接口：TalkBotGPT 提供简单易用的接口，可以与其他应用或服务无缝集成，实现对话功能的可扩展性和定制性。

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

## Contributing
我们欢迎社区的贡献！如果您想为 TalkBotGPT 做贡献，请查阅[贡献指南](CONTRIBUTING.md)以获取详细信息和开始的方法。

## License
TalkBotGPT 是一款开源软件，根据[MIT License](LICENSE)进行许可。请根据许可证的条款自由使用、修改和分发。

## Contact Us

如果您有任何问题、建议或反馈，请随时[联系我们](mailto:tinyzqh@163.com)。我们欢迎您的意见，并乐意协助解答任何疑问。谢谢您的支持！


TalkBotGPT 是一个功能强大的对话式聊天机器人项目，为开发者和用户提供丰富的对话生成能力，帮助他们构建智能、灵活、可定制的对话应用。无论是用于商业应用还是个人项目，TalkBotGPT 都可以为用户带来便利和创新。
