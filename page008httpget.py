import urllib.request
keyword="Hello"
url="http://www.baidu.com/s?wd="+keyword
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("C:/Users/Administrator/Desktop/page008.html",'wb')
fhandle.write(data)
fhandle.close()

