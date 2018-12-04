import urllib.request
import urllib.error
try:
    urllib.request.urlopen("https://bolg.csdn.net")
except urllib.error.URLError as e:
    print(e.errno)
    print(e.reason)
except urllib.error.HTTPError as e:
    print(e.errno)
    print(e.reason)
