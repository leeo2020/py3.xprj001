import urllib.request
keyword="韦玮老师"
key_code=urllib.request.quote(keyword)
url="http://www.baidu.com/s?wd="+key_code
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("C:/Users/Administrator/Desktop/page009.html",'wb')
fhandle.write(data)
fhandle.close()
print(key_code)
print(url)