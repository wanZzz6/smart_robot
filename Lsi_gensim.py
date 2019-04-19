import jieba
from gensim import corpora
from gensim import models
from gensim import similarities

l1 = ["你的名字是什么", "你今年几岁了", "你会敲代码吗", '你会干什么', '屏幕截图',
      '我想听音乐', '我想敲代码', '百度搜索', '播放音乐', '打开记事本']  # 标准问题


# dictionary = []
# lsi = []

def get_index_matrix():
    global l1, dictionary, lsi
    # if 'Lsi_matrix.index' in os.listdir('.'):
    #     index = similarities.SparseMatrixSimilarity.load('Lsi_matrix.index')
    #     return index
    all_doc_list = [list(jieba.cut(doc)) for doc in l1]
    # 制作词袋
    dictionary = corpora.Dictionary(all_doc_list)
    # 语料库:
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    # 将corpus语料库(初识语料库) 使用Lsi模型进行训练
    lsi = models.LsiModel(corpus)
    # 文本相似度
    # 稀疏矩阵
    index = similarities.SparseMatrixSimilarity(
        lsi[corpus], num_features=len(dictionary.keys()))

    index.save('Lsi_matrix.index')
    # index = similarities.SparseMatrixSimilarity.load('Lsi_matrix.index')
    return index


def get_high_sim(doc, index_matrix):
    doc_test_list = list(jieba.cut(doc))
    # 将需要寻找相似度的分词列表 做成 语料库 doc_test_vec
    doc_test_vec = dictionary.doc2bow(doc_test_list)
    sim = index_matrix[lsi[doc_test_vec]]

    # 对下标和相似度结果进行一个排序,拿出相似度最高的结果
    cc = sorted(enumerate(sim), key=lambda item: -item[1])
    print(cc)
    high_score = cc[0]
    text = l1[high_score[0]]

    print(doc, '-------', text)
    print('相似度：', high_score[1])
    if high_score[1] > 0.6:
        return cc[0][0]


index = get_index_matrix()

if __name__ == '__main__':
    a = "你今年多大了"
    doc_index = get_high_sim(a, index)
    print(doc_index)
