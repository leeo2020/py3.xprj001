import urllib.request
import urllib.error

try:
    # urllib.request.urlopen("http://blog.baidusss.net")
    urllib.request.urlopen("https://user.qzone.qq.com/1013275748/infocenter")
except urllib.error.HTTPError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)


