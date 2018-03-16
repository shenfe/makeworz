import jpype
from util import os_type, view_conllu, read_json

hanlp_path = "./vendor/hanlp/"

jvm_path = jpype.getDefaultJVMPath()

mem_limit = "1g"


def start_jvm():
    """
    启动JVM
    """
    jpype.startJVM(jvm_path,
                   "-Djava.class.path=%shanlp-1.5.4.jar%s%s" % (
                       hanlp_path, ";" if (os_type() == 0) else ":", hanlp_path),
                   "-Xms%s" % mem_limit,
                   "-Xmx%s" % mem_limit)
    jpype.java.lang.System.out.println("jvm started")


def segment(text):
    """
    分词
    """
    hanlp = jpype.JClass("com.hankcs.hanlp.HanLP")
    return hanlp.segment(text)


def ner_pos(text):
    """
    命名实体识别与词性标注
    """
    nlptokenizer = jpype.JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
    return nlptokenizer.segment(text)


def keyword(text, num=2):
    """
    关键词提取
    """
    hanlp = jpype.JClass("com.hankcs.hanlp.HanLP")
    return hanlp.extractKeyword(text, num)


def summary(text):
    """
    自动摘要
    """
    hanlp = jpype.JClass("com.hankcs.hanlp.HanLP")
    return hanlp.extractSummary(text, 3)


def parse_dep(text):
    """
    依存句法分析
    """
    hanlp = jpype.JClass("com.hankcs.hanlp.HanLP")
    return hanlp.parseDependency(text)


def stop_jvm():
    """
    关闭JVM
    """
    jpype.java.lang.System.out.println("jvm stopping")
    jpype.shutdownJVM()


if __name__ == '__main__':
    start_jvm()

    # 分词
    print(segment("你好，欢迎在Python中调用HanLP的API"))
    testCases = [
        "商品和服务",
        "结婚的和尚未结婚的确实在干扰分词啊",
        "买水果然后来世博园最后去世博会",
        "中国的首都是北京",
        "欢迎新老师生前来就餐",
        "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
        "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]
    for sentence in testCases:
        print(segment(sentence))

    # ner & pos
    print(ner_pos("中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程"))

    document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
               "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
               "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
               "严格地进行水资源论证和取水许可的批准。"

    # 提取关键词
    print(keyword(document, 3))

    # 自动摘要
    print(summary(document))

    # 句法分析
    view_conllu(list(map(parse_dep, testCases + ["徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"])))
    view_conllu(list(map(parse_dep, read_json("./data/source.json"))))

    stop_jvm()
