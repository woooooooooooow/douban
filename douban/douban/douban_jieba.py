# encoding=utf-8
#分词&去停用词，可用

import jieba
import codecs

#加载停用词表
stop1 = [line.strip() for line in open('stop.txt', 'r', encoding='utf-8').readlines()]
stop2 = [line.strip() for line in open('douban_content_jieba_cipin5.txt', 'r', encoding='utf-8').readlines()]
stop = stop1 + stop2

#加载用户自定义词典
jieba.load_userdict("userdict.txt")

fr = codecs.open('short_riview.txt',encoding='utf-8')
fw = codecs.open('short_riview_jieba.txt','w',encoding='utf-8')

for line in fr:
    final = ''
    newline = jieba.cut(line)
    newline = list(newline)
    print(newline)
    for seg in newline:
        # 去停用词
        if seg not in stop:
            final += ' ' + seg
    print(final)
    fw.write(final)

fr.close()
fw.close()