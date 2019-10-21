'''
开发人员：赵吉宁
脚本功能：进度条
开发时间：2019-09-04
'''
from tqdm import tqdm

import time

text=''
for i in tqdm(['a','b','c','d','d','d','d','d','d','d','d','d','d','d','d']):
    text=text+i
    time.sleep(0.1)


print('text字符串为：',text)

for i in tqdm(range(10000000)):
    pass

