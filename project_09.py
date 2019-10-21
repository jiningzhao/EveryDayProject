import xlsxwriter
import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import urllib
import json
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
a=open('/Users/tq/Desktop/BYSJ/json1/icon.json')
a=json.load(a)

w=[]
d=[]
b=a.get('constant').get('urlPrefix').get('assets')  #前缀
print(b)
c=a.get('screen')
for i in c:
  for j in c.get(i):
    for k in c.get(i).get(j):
      w.append(k)
      print(k)
  # print(c[i])
print(c)


print("####################"*5)
for l in w:
  print(l)
  if l.get('name') == 'Grid' or l.get('name') == 'DiamondZone':
    print(l.get('config').get('apps'))
    for i in l.get('config').get('apps'):
      j={}
      print(d.append({'title':i.get('title'),'icon':b+i.get('icon')}))
      print(i.get('icon'))


print("###"*100)
for i in d:
  print(i)
def save_img(img_url,file_name,file_path='/Users/tq/Desktop/BYSJ/img/'): # 将图片拼接下载后，加上名称title存储到文件夹中
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误 ：',e)
def icon(d): # 将想要排列的第一列与第二列分别放在两个list中
  movies=[[],[]]
  for i in d:
    a1=i.get('title')
    a2=i.get('icon')
    if a1 in movies[0]:
      a1 = a1 + "1"
    movies[0].append(a1)
    movies[1].append(a2)

    save_img(a2,a1)

  return movies

def Xlsx(d): # 把拼接的结果写到xlsx文档中
  movies = icon(d)

  xlsx = xlsxwriter.Workbook("/Users/tq/Desktop/BYSJ/xlsx/icon.xlsx")
  sht = xlsx.add_worksheet()
  k = 0
  for movie_name in movies[0]:
    sht.write(k, 0, movie_name)
    k += 1
  k = 0
  for movie_href in movies[1]:
    sht.write(k, 1, movie_href)
    k += 1
  xlsx.close()

Xlsx(d)

