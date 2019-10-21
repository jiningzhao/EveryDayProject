'''
脚本功能：爬虫并保存到表格
开发人员：赵吉宁
开发时间：2019-7-26 星期五
'''
import xlsxwriter
import requests
from bs4 import BeautifulSoup
from urllib import request
#-------------------------------------------------------------------
'''
Python 2.7.9 之后版本引入了一个新特性

当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 

当目标使用的是自签名的证书时就会爆出一个

urllib.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)> 的错误消息
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#-------------------------------------------------------------------

class Spider():
    def __init__(self,url):
        self.url = url


    def Headers(self):
        # 请求头信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        return self.headers

    def Get_html(self):
        # 获取网站的源码
        self.html = requests.get(self.url, headers=self.Headers()).content
        return self.html

    def Soup(self):
        # BeautifulSoup解析
        self.soup = BeautifulSoup(self.Get_html(), features='lxml')
        return self.soup

    def Print(self):
        self.movie_list=[[],[],[]]
        self.links = self.Soup().find_all(attrs={"class":"nbg"})
        for i in self.links:
            j=i.find("img")
            self.movie_list[2].append(j.get("src"))
            print(j.get("src"))
        for link in self.links:
            movie_imgs=link.get("href")
            movie_names=link.get('title')
            self.movie_list[1].append(movie_imgs)
            self.movie_list[0].append(movie_names)
            print(link.get('title'),link.get("href"))
        return self.movie_list

    def Xlsx(self):
        movies = self.Print()
        self.xlsx=xlsxwriter.Workbook("/Users/tq/Desktop/BYSJ/xlsx/movies.xlsx")
        sht=self.xlsx.add_worksheet()
        k=0
        for movie_name in movies[0]:
            sht.write(k,0,movie_name)
            k+=1
        k=0
        for movie_href in movies[1]:
            sht.write(k,1,movie_href)
            k+=1
        k=0
        for movie_src in movies[2]:
            sht.write(k,2,movie_src)
            request.urlretrieve(movie_src,"/Users/tq/Desktop/BYSJ/img/"+str(k)+".jpg")

            k+=1
        k=0
        for movie_num in range(len(movies[0])):
            sht.write(k,3,movie_num)
            k+=1
        self.xlsx.close()


if __name__ == "__main__":
    url = "https://movie.douban.com/chart"
    a=Spider(url)
    a.Xlsx()
