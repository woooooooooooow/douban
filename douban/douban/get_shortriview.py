import pymysql
#从数据库里读某个字段，去掉字段中的换行，写入txt文件，可用

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', user='root', passwd='2333', db='douban', charset="utf8mb4", use_unicode=True)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "select review from short_review"
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
number = cursor.fetchall()
file = open('short_riview.txt', mode='a', encoding='utf8')
loan_count = 0
for loanNumber in number:
    loan_count += 1
    eachline = str(loanNumber[0]).replace(" ","").replace("\n","")
    file.write(eachline + "\n" )
file.close()
db.close()