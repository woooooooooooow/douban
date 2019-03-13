# -*- coding: utf-8 -*-
import os
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
from pyltp import SementicRoleLabeller

sentence = '我家在昆明，我现在在北京上学。中秋节你是否会想到李白？'
def sentence_splitter(sentence):
    LTP_DATA_DIR = 'E:\python\ltp_data_v3.4.0'  # ltp模型目录的路径
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
    sents = SentenceSplitter.split(sentence)  # 分句
    print('\n'.join(sents))

#测试分句
#sentence_splitter(sentence)

#分词
def segmentor(sentence):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('E:\python\ltp_data_v3.4.0\cws.model')  # 加载模型
    segmentor.load_with_lexicon('E:\python\ltp_data_v3.4.0\cws.model', 'E:/python/douban/douban/userdict.txt')
    words = segmentor.segment(sentence)  # 分词
    #默认可以这样输出
    # print '\t'.join(words)
    # 可以转换成List 输出
    words_list = list(words)
    for word in words_list:
        print(word)
    segmentor.release()  # 释放模型
    return words_list

#测试分词
#segmentor(sentence)

def posttagger(words):
    postagger = Postagger() # 初始化实例
    postagger.load('E:\python\ltp_data_v3.4.0\pos.model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    for word,tag in zip(words,postags):
        print(word+'/'+tag)
    postagger.release()  # 释放模型
    return postags
#测试标注
words = segmentor(sentence)
tags = posttagger(words)

def ner(words, postags):
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load('E:/python/ltp_data_v3.4.0/ner.model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    for word, ntag in zip(words, netags):
        print(word + '/' + ntag)
    recognizer.release()  # 释放模型
    return netags

#测试命名实体识别
ner(words,tags)

def parse(words, postags):
    parser = Parser() # 初始化实例
    parser.load('E:/python/ltp_data_v3.4.0/parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()  # 释放模型

#测试句法分析
words = segmentor(sentence)
tags = posttagger(words)
parse(words, tags)

def role_label(words, postags, netags, arcs):
    labeller = SementicRoleLabeller() # 初始化实例
    labeller.load('E:/python/ltp_data_v3.4.0/pisrl.model')  # 加载模型
    roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
    for role in roles:
        print(role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
    labeller.release()  # 释放模型

words = segmentor(sentence)
tags = posttagger(words)
#命名实体识别
netags = ner(words,tags)
#依存句法识别
arcs = parse(words,tags)
#语义角色标注
roles = role_label(words,tags,netags,arcs)
