# !/usr/bin/python
# -*- coding:utf-8 -*-

from gensim import corpora,models
from collections import defaultdict
import codecs
import numpy as np

#参数初始化
file=codecs.open('test.txt','r','utf-8')
'''
frequency = defaultdict(int)
texts=[]
for eachLine in file.readlines():
    lineList = eachLine.split(' ')
    for item in lineList:
        frequency[item]+=1
        #print(frequency)
    texts.append([item for item in lineList if item!='\n' and item!='\r\n' and frequency[item] > 1 ])  #去除换行符和只出现一次的词
print(texts)
'''
texts=[]
for eachLine in file.readlines():
    lineList = eachLine.split(' ')
    texts.append([item for item in lineList if item!='\n' and item!='\r\n'])  #去除换行符和只出现一次的词
print(texts)

