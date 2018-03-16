import synonyms


def segment(text):
    """
    分词
    """
    return synonyms.seg(text)


def nearby(word):
    """
    相近词
    """
    return synonyms.nearby(word)


def compare(text1, text2, seg=True):
    """
    相似度
    """
    return synonyms.compare(text1, text2, seg)


if __name__ == '__main__':
    # 分词
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

    # 相近词
    print(nearby("中国"))
    print(nearby("喜欢"))
    print(nearby("买房"))

    # 相似度
    print(compare("我喜欢财富", "我爱钱"))
    print(compare("我喜欢财富", "我喜欢文学"))
