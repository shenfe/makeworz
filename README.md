# makeworz

## Requirements

* Python 3.x
* Java 8

## Vendors

* [HanLP](https://github.com/hankcs/HanLP)
* [Synonyms](https://github.com/huyingxi/Synonyms)

## Commands

```bash
$ python -m venv .py3env                    # 创建venv环境
$ source .py3env/bin/activate               # 进入venv环境（unix/linux）
$ source .py3env/Scripts/activate           # 进入venv环境（cygwin）
$ .py3env\Scripts\activate                  # 进入venv环境（windows）
(.py3env) $ pip install -r requirements.txt # 安装依赖
(.py3env) $ pip install scipy               # 安装一个包
(.py3env) $ pip freeze > requirements.txt   # 保存安装包清单
(.py3env) $ deactivate                      # 退出venv环境
```
