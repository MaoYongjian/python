import urllib.request
url = 'http://www.baidu.com'
print('第一种方法')
request1 = urllib.request.urlopen(url)
html = request1.read()
print(len(html))
print(request1.getcode())


# header = {'user-agent':'Mozilla/5.0'}
# req = urllib.request.Request(url)
# req.add_header(header)
# response = urllib.request.urlopen(req)
# the_page = response.getcode()
# print(the_page)
# print(len(response.read()))


url = 'http://baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers1 = { 'User-Agent' : user_agent }
req = urllib.request.Request(url,headers=headers1)
html1 = urllib.request.urlopen(req)
print(html1.getcode())

print('第三种方法')


# 解析器
print('解析器')
from bs4 import BeautifulSoup
# 创建BeautifulSoup对象
# soup = BeautifulSoup(
# 					html_doc,
# 					'html.parser',
# 					from_encoding='utf-8'	)

#搜索节点(find_all,find)
# 标签,条件,内容
# find_all('div',class=' one',string='python')
# find_all(name,attrs,string )

# 使用get_text()获取文字

html_doc = '''
	<div class="one">
		<div class="text">
			dsa
		</div>
	</div>
	<div class="two">
		<div class="text1">
			321314
		</div>
	</div>'''
div2 = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

div1 = div2.find_all('div',class_='text1')
for div in div1:
	print(div.get_text())