# !/usr/bin/python
# -*- coding:utf-8 -*-
#lda 加 可视化，可用

from gensim import corpora,models
from collections import defaultdict
import codecs
import numpy as np
import pyLDAvis
import pyLDAvis.sklearn
import pyLDAvis.gensim

#参数初始化
file=codecs.open('short_riview_jieba.txt','r','utf-8')

'''
frequency = defaultdict(int)
texts=[]
for eachLine in file.readlines():
    lineList = eachLine.split(' ')
    for item in lineList:
        frequency[item]+=1
        print(frequency)
    texts.append([item for item in lineList if item!='\n' and item!='\r\n' and frequency[item] > 1 ])  #去除换行符和只出现一次的词
print(texts)
'''

texts=[]
for eachLine in file.readlines():
    lineList = eachLine.split(' ')
    texts.append([item for item in lineList if item!='\n' and item!='\r\n'])

#建立词典
dict=corpora.Dictionary(texts)
#建立语料库
corpus = [dict.doc2bow(i) for i in texts]
#LDA模型训练
lda = models.LdaModel(corpus,num_topics=5, id2word=dict, alpha=0.1, eta=0.005, minimum_probability=0.01,
                            update_every=1, chunksize=5000, passes=10, eval_every=1, iterations=2000)
#lda.print_topics(10,5)

file = codecs.open('short_LDA_result.txt', 'a', 'utf-8')
for topic in lda.print_topics(num_words=20):   #输出每个主题下的前20个词
	file.write(str(topic)+'\n')
	print(topic)

data = pyLDAvis.gensim.prepare(lda, corpus, dict)
pyLDAvis.show(data, open_browser=False)

doc_topics=lda.get_document_topics(corpus) #所有文档的主题分布
#print(doc_topics)
idx=np.arange(len(texts))
#print(idx)
np.random.shuffle(idx)
#建立存储微博分类结果的主题列表  （哈哈哈哈，不知道怎么循环建，就是这么啰嗦）
topic_doc0 = []
topic_doc1 = []
topic_doc2 = []
topic_doc3 = []
topic_doc4 = []
topic_doc5 = []
topic_doc6 = []
topic_doc7 = []
topic_doc8 = []
topic_doc9 = []

for i in idx:
	topic = np.array(doc_topics[i])
	#print(topic)
	topic_distribute = np.array(topic[:,1])
	#print(topic_distribute)
	topic_most_pr = topic_distribute.argmax()          #取文档——主题分布中，最大概率的主题作为该文档所属主题
	#print('doc: {} ,best topic: {}'.format(i, topic_most_pr))
	#将文档主题匹配，写入分类列表
	if topic_most_pr == 0:
		topic_doc0.append(i)
	if topic_most_pr==1:
		topic_doc1.append(i)
	if topic_most_pr==2:
		topic_doc2.append(i)
	if topic_most_pr==3:
		topic_doc3.append(i)
	if topic_most_pr==4:
		topic_doc4.append(i)
	if topic_most_pr==5:
		topic_doc5.append(i)
	if topic_most_pr==6:
		topic_doc6.append(i)
	if topic_most_pr==7:
		topic_doc7.append(i)
	if topic_most_pr==8:
		topic_doc8.append(i)
	if topic_most_pr==9:
		topic_doc9.append(i)

	filePath = 'E:/python/douban/lda_num/'
	topicFile = 'Topic' + str(topic_most_pr) + '.csv'  # 把句子序号写入主题下
	with codecs.open(filePath + topicFile, 'a', 'utf-8') as file2:
		file2.writelines(str(i) + '\n')

#输出主题，主题下的微博数，以及微博标号
print('topic0',len(topic_doc0))
print('topic1',len(topic_doc1))
print('topic2',len(topic_doc2))
print('topic3',len(topic_doc3))
print('topic4',len(topic_doc4))
print('topic5',len(topic_doc5))
print('topic6',len(topic_doc6))
print('topic7',len(topic_doc7))
print('topic8',len(topic_doc8))
print('topic9',len(topic_doc9))



'''

#将微博分别写入主题之下
#将摘要分别写到不同的主题中
file2 = codecs.open( 'E:/python/douban/lda_num/allweibo_top.txt', 'r', 'utf-8')
texts1 = file2.readlines()
for item in topic_doc0:
	text1 = texts1[item]
	print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos1.txt', 'a', 'utf-8')as f1:
		f1.writelines(text1)
for item in topic_doc1:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos2.txt', 'a', 'utf-8')as f2:
		f2.writelines(text1)
for item in topic_doc2:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos3.txt', 'a', 'utf-8')as f3:
		f3.writelines(text1)
for item in topic_doc3:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos4.txt', 'a', 'utf-8')as f4:
		f4.writelines(text1)
for item in topic_doc4:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos5.txt', 'a', 'utf-8')as f5:
		f5.writelines(text1)
for item in topic_doc5:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos6.txt', 'a', 'utf-8')as f6:
		f6.writelines(text1)
for item in topic_doc6:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos7.txt', 'a', 'utf-8')as f7:
		f7.writelines(text1)
for item in topic_doc7:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos8.txt', 'a', 'utf-8')as f8:
		f8.writelines(text1)
for item in topic_doc8:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos9.txt', 'a', 'utf-8')as f9:
		f9.writelines(text1)
for item in topic_doc9:
	text1 = texts1[item]
	#print(text1)
	with codecs.open('E:/python/douban/lda_num/weibos10.txt', 'a', 'utf-8')as f10:
		f10.writelines(text1)

'''

