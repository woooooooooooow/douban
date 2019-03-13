import requests
import json
import xlwt
import csv
import random
import time
from lxml import etree
import pymysql

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0'
]

def Douban():
    #爬豆瓣长影评id
    for start in range(14000, 15000, 20):
        print(start)
        headers = {
            'User-Agent': random.choice(user_agents)
             }
        file = open('douban14.txt', mode='a', encoding='utf8mb4')
        #proxies = {'https': 'https://222.135.31.67:8060'}
        start_url = "https://movie.douban.com/subject/26752088/reviews?start="+str(start)
        def GetReviewid(url):
           # res = requests.get(url, headers=headers, proxies=proxies)
            res = requests.get(url, headers=headers)
            html_doc = res.content.decode("utf8mb4")
            tree = etree.HTML(html_doc)
            datas_id = tree.xpath('//*[@id="content"]/div/div[1]/div[1]//div/@data-cid')
            for data_id in datas_id:
                print(data_id)
                file.write('\n' + str(data_id))
        GetReviewid(start_url)
        time.sleep(random.randint(0, 3))

# Douban()

def ReadReviewId():
    #从txt里读reviewid
    result=[]
    with open('douban12.txt', 'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    return result

def DoubanSpider():
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='2333', db='douban', charset="utf8mb4", use_unicode=True)
    #从text中取review的ID
    ids = ReadReviewId()
    for id in ids:
        id = ''.join(id)
        headers = {
            'User-Agent': random.choice(user_agents)
        }
        url = "https://movie.douban.com/review/"+str(id)+"/"
        res = requests.get(url, headers=headers)
        res = res.content.decode("utf8")
        tree = etree.HTML(res)
        path1 = '//*[@id="link-report"]/div[1]/p/text()'
        content = tree.xpath(path1)
        path2 = '// *[ @ id = '+str(id)+'] / header / span[2]/text()'
        score = tree.xpath(path2)
        path3 = '// *[ @ id = '+str(id)+'] / header / a[1] / span/text()'
        name = tree.xpath(path3)
        score = ''.join(score)
        name = ''.join(name)
        content = ''.join(content)
        print(id)
        print(name)
        print(score)
        print(content)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "insert into review(id,name,score,content)values('{}','{}','{}','{}')".format(id, name, score, content)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            print("插入数据库失败")
            db.rollback()
            continue
        time.sleep(random.randint(0, 1))
    #关闭数据库连接
    db.close()

DoubanSpider()

'''
textname = id+'.txt'
file = open(textname, mode='a', encoding='utf-8')
file.write(str(id) + '\n')
file.write(str(name) + '\n')
file.write(str(score) + '\n')
file.write(str(content) + '\n')

contentlist = []
contentlist[0] = id
contentlist[1] = str(name)
contentlist[2] = str(score)
contentlist[3] = str(content)
out = open('CONTENT.csv', 'a', encoding='utf-8')
csv_write = csv.writer(out, dialect='excel')
csv_write.writerow(contentlist)
'''


