'''
开发人员：赵吉宁
脚本功能：计算圆周率
开发时间：2019-09-05
'''
from random import random
from time import perf_counter
from tqdm import tqdm
DARTS = 10000*10000
hits = 0.0
start = perf_counter()
for i in tqdm(range(1,DARTS+1)):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2,0.5)
    if dist <= 1.0:
        hits = hits +1
pi = 4 * (hits/DARTS) #根据概率求圆的面积
print("圆周率值为：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))
