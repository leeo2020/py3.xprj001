import urllib.request
url="https://blog.csdn.net/weiwei_pig/article/details/51178226"
req=urllib.request.Request(url)
req.add_header("User-Agent","User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)")
data=urllib.request.urlopen(req).read()

fhandle=open("C://Users//Administrator//Desktop//page000.html","wb")
fhandle.write(data)
fhandle.close
print(data)