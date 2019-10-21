'''
开发人员：赵吉宁
脚本功能：爬取《中国文旅门户网》个别字段信息
时间：2019-8-3 星期六
'''

from bs4 import BeautifulSoup
import requests
#网页头信息
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
# ---------------获得网页的源码--------------------
html=requests.get("http://www.cntour.cn/",headers=headers).text

# 使用BeautifulSoup来解析网页：使用lxml解析器进行解析
soup=BeautifulSoup(html,'lxml')

# -------------对网页元素进行定位-------------------
data=soup.select("#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a")

# -----------设置列表存放爬取的数据-----------------
a=[]

# --------循环将爬取的数据进行数据清洗--------------
for i in data:
    a.append({
        "href":i.get("href"),
        "name":i.get_text()
    })

# -----------输出爬取的未清洗的数据-----------------
print(data)

# ------------循环输出清洗后的数据------------------
for j in a:
    print(j)