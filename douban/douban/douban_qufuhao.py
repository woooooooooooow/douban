#!/usr/bin/env python
# coding=utf-8
#去英文标点符号+中文标点符号,可用,但是去完不分行，已添加到停用词表，直接用jieba.py
from string import punctuation
import re
import sys
import codecs

# 英文标点符号+中文标点符号
punc = punctuation + u'.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：❤😤😂△0123456789qazwsxedcrfvtgbyhnujmiklopQAZWSXEDCRFVTGBYHNUJMIKLOP'

print(punc)

fr = codecs.open('douban_content_jieba.txt',encoding='utf-8')
fw = codecs.open('douban_content_jieba_去符号.txt','w',encoding='utf-8')

# 利用正则表达式替换为一个空格
for line in fr:
    line = re.sub(r"[{}]+".format(punc), "", line)
    line = line + "\n"
    fw.write(line)

fr.close()
fw.close()