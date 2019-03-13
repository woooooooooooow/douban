# ecoding=utf-8
#去掉文件里所有的空格，可用

def stripFile(oldFName,newFName):
  '''''remove the space or Tab or enter in a file,and output to a new file in the same folder'''
  fp = open(oldFName, "r+", encoding="utf8")
  newFp = open(newFName, "w", encoding="utf8")
  for eachline in fp.readlines():
    newStr = eachline.replace(" ","").replace("\t","").strip()
    #print "Write:",newStr
    newFp.write(newStr)
  fp.close()
  newFp.close()
if __name__ == "__main__":
  oldName = "douban_content.txt"
  newName = "douban_content_out.txt"
  stripFile(oldName , newName)


