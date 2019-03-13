# encoding=utf-8
#结巴分词，仅分词，可用
import jieba
import codecs


fr = codecs.open('douban_content.txt',encoding='utf-8')
fw = codecs.open('douban_content_out.txt','w',encoding='utf-8')

jieba.load_userdict("userdict.txt")

for line in fr:
    newline = jieba.cut(line)
    fw.write(" ".join(newline))

fr.close()
fw.close()

