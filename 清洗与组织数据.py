import requests
from bs4 import BeautifulSoup
import re

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

html=requests.get('http://www.cntour.cn/',headers).text

soup=BeautifulSoup(html,'lxml')

data=soup.select("#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a")

for i in data:
    result={
        'link':i.get('href'),
        'title':i.get_text(),
        'ID':re.findall('\d+',i.get('href'))
    }
    print(result)
