import urllib.request
# 链接域名
f = urllib.request.urlopen('http://www.baidu.com')
f1 = urllib.request.urlopen('http://www.quchuangye.net.cn/')

# 不存在的域名
f2 = urllib.request.urlopen('http://www.quchuangy.net.cn/')
# 读取内容
html = f.read()
# 返回远程HTTPMessage对象的头信息
info1 = f.info()
info2 = f1.info()

# 返回http状态码,200表示链接成功,404表示为找到页面
getcode1 = f.getcode()
getcode2 = f2.getcode()
print(getcode1)
print(getcode2)