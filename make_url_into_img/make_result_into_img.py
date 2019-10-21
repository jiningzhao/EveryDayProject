'''
开发者：赵吉宁
脚本功能：将json文件中的icon、图片地址拼接下载到本地文件夹
时间：2019-10-18
'''
import json_processing
import urllib
from urllib import request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

json_processing.Json_Process().first_key() # 调用json_processing文件中的方法，拿到cover、icon、assets参数备用

class Make_img():

    def __init__(self):
        self.icon = json_processing.icon
        self.cover = json_processing.cover

    def cover_img(self,img_url, file_name, file_path='/Users/tq/Desktop/BYSJ_Git/cover_img/'):  # 将图片拼接下载后，加上名称title存储到文件夹中（2）
        # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
        try:
            if not os.path.exists(file_path):
                print('文件夹', file_path, '不存在，重新建立')
                # os.mkdir(file_path)
                os.makedirs(file_path)
            # 获得图片后缀
            file_suffix = os.path.splitext(img_url)[1]
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)
        except IOError as e:
            print('文件操作失败', e)
        except Exception as e:
            print('错误 ：', e)

    def icon_img(self,img_url, file_name, file_path='/Users/tq/Desktop/BYSJ_Git/icon_img/'):  # 将图片拼接下载后，加上名称title存储到文件夹中（3）
        # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
        try:
            if not os.path.exists(file_path):
                print('文件夹', file_path, '不存在，重新建立')
                # os.mkdir(file_path)
                os.makedirs(file_path)
            # 获得图片后缀
            file_suffix = os.path.splitext(img_url)[1]
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)
        except IOError as e:
            print('文件操作失败', e)
        except Exception as e:
            print('错误 ：', e)
    def demo(self):
        n = 0
        for i in self.cover:
            n = n+1
            cover_title = str(n)
            cover_line = json_processing.assets[0] + i.get('cover')
            self.cover_img(cover_line,cover_title)

        for i in self.icon:
            icon_title = i.get('title')
            icon_line = json_processing.assets[0] + i.get('icon')
            self.icon_img(icon_line,icon_title)

if __name__ == '__main__':
    Make_img().demo()