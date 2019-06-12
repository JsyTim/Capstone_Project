import logging
from gensim import models
import numpy as np


def calculate():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)
    model = models.Word2Vec.load("G:/model/wiki_corpus.model")
    one_corpus = ["三毛"]
    result = model.most_similar(one_corpus[0], topn=30)
    print(result)
    # 输入一个词找出相似的前10个词
    #将返回的结果转换为字典,便于绘制词云
    # word_cloud = dict()
    # for sim in result:
    #     # print(sim[0],":",sim[1])
    #     word_cloud[sim[0]] = sim[1]


    # 输入两个词计算相似度
    two_corpus = ["张爱玲", "林语堂"]
    res = model.similarity(two_corpus[0], two_corpus[1])
    # print("similarity:%.4f" % res)


if __name__ == "__main__":
    calculate()
