import platform
import time
import codecs
import os
import subprocess
import sys
from functools import reduce


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
