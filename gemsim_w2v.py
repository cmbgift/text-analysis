# 引入 word2vec
from gensim.models import word2vec

#https://zhuanlan.zhihu.com/p/24961011
#https://www.cnblogs.com/pinard/p/7278324.html w2v 训练的一些要点
# 引入日志配置
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs","yoyoyo you go home now to sleep"]
# 切分词汇
sentences= [s.split() for s in raw_sentences ]
# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1)
# 进行相关性比较
print(model.similarity('dogs','you'))
print(model.most_similar(['you']))
print(model['you'].shape)
print(type(model['you']))
"""
模型保存
model.save('text8.model')
模型读取
model1 = Word2Vec.load('text8.model')
"""