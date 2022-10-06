# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 取石子游戏.py
@time: 2022/10/6 23:04
"""
import math

a = 2
b = 1
if a > b:
    a, b = b, a


def qiyi(n):
    temp = int(n / 2 * (1 + math.sqrt(5)))
    if (a == temp) and (b == a + n):
        return 1
    else:
        return 0


for i in range(a + 1):
    if qiyi(i):
        print('Loose')
        break
else:
    print('Win')
