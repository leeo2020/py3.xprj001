import urllib.request
import os
url=urllib.request.quote("https://blog.csdn.net/weiwei_pig/article/details/51178226")
url="https://blog.csdn.net/weiwei_pig/article/details/51178226"
headers=("User-Agent","User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
# file=urllib.request.openurl(url)
fhandle=open("C://Users//Administrator//Desktop//page00.html","wb")
fhandle.write(data)
fhandle.close
print(data)