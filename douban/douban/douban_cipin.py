# encoding=utf-8
#分词 + 去停用 + 统计低频次 + 将低频词写入停用词词典
import jieba
import codecs

getTF_alltxt_dic = {}

#加载停用词表
stop = [line.strip() for line in open('stop.txt', 'r', encoding='utf-8').readlines()]
#加载用户自定义词典
jieba.load_userdict("userdict.txt")

fr = codecs.open('douban_content.txt',encoding='utf-8')
fw = codecs.open('douban_content_jieba3.txt','w',encoding='utf-8')
getTF_result = codecs.open('douban_content_jieba_cipin5.txt', 'a', encoding='utf-8')

getTF_singletxt_dic = {}
for line in fr:
    final = ''
    newline = jieba.cut(line)
    newline = list(newline)
    print(newline)
    for seg in newline:
        # 去停用词
        if seg not in stop:
            final += ' ' + seg
            if seg in getTF_singletxt_dic:
                getTF_singletxt_dic[seg] += 1
            else:
                getTF_singletxt_dic[seg] = 1
    print(final)
    fw.write(final)

for a, b in getTF_singletxt_dic.items():
    if b < 6:
        print(a,b)
        getTF_result.write(a + "\r\n")

fr.close()
fw.close()
getTF_result.close()

