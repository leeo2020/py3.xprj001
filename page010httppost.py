import urllib.request
import urllib.parse
url="http://www.iqianyue.com/mypost/"
poatdata=urllib.parse.urlencode({
    "name":"ceo@iqianyue.com","pass":"aA123456"
}).encode('UTF-8')
req=urllib.request.Request(url,poatdata)
req.add_header('User-Agent',"User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)")
data=urllib.request.urlopen(req).read()
fhandle=open("C:/Users/Administrator/Desktop/page010.html",'wb')
fhandle.write(data)
fhandle.close()

