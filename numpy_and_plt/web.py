
import urllib.request as req
res = req.urlopen('http://www.google.co.kr')
data = res.read().decode('euc-kr')
f = open('google.html', 'w', encoding='utf8')
f.write(data)
f.close()