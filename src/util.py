import platform
import time
import codecs
import os
import subprocess
import sys
from functools import reduce
import json
import re


def open_file(filepath):
    filepath = os.path.normpath(filepath)
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))
    elif os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filepath))


def os_type():
    t = platform.system()
    print("platform is ", t)
    if t == 'Windows':
        return 0
    return 1


def read_json(filepath):
    data = {}
    filepath = os.path.normpath(filepath)
    with codecs.open(filepath, 'r', encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    return data


def view_conllu(code):
    if not isinstance(code, list):
        code = [code]
    code = reduce(lambda x, y: x + ('<code class="conllu-parse" tabs="yes"><pre>%s\n</pre></code>' % str(y)), code, "")
    fp = open("./vendor/conllu.js/template.html", "r")
    html = fp.read().replace("__code__", code)
    fp.close()
    filepath = "./vendor/conllu.js/output_%s.html" % time.time()
    fp = codecs.open(filepath, "w", "utf-8")
    fp.write(html)
    fp.close()
    open_file(filepath)


def split(text):
    """
    断句
    """
    groups = list(filter(lambda t: t != "", re.split("[。！？]+", text)))
    if len(groups) == 1:
        return re.split("[，；]+", text)
    return list(map(split, groups))


if __name__ == '__main__':
    # data = read_json("data/source.json")
    # print(data[:1])

    text = "我是南方人，但喜欢北方蓝天。你和我一样吗？好吧，原来不一样！"
    print(split(text))
    text1 = "我是南方人"
    print(split(text1))
