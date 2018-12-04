# from urllib3 import *
import urllib.request
import os
path=os.path
file=urllib.request.urlopen("https://www.baidu.com")
data=file.read()
# dataline=file.readline()
# datalines=file.readlines()file
# print(dataline)
# print(datalines)
print(data)
print(file.info())
print(file.getcode())
print(file.geturl())
#写入并保存本地文件
fhandle=open("C://Users//Administrator//Desktop//page01.html","wb")
fhandle.write(data)
fhandle.close

#直接写入并保存本地文件
filename=urllib.request.urlretrieve("https://edu.51cto.com",filename="C://Users//Administrator//Desktop//page11.html")
urllib.request.urlcleanup

url=urllib.request.quote("https://www.sina.com.cn")
print(url)
url=urllib.request.unquote("https://www.sina.com.cn")
print(url)