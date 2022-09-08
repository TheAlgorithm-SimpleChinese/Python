# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 三角形形状.py
@time: 2022/9/2 16:10
"""
a = 3.0
b = 4.0
c = 5.0
lis = [a, b, c]
lis.sort()

if lis[0] + lis[1] <= lis[2]:
    print('W')  # 不能组成三角形
else:
    if lis[0] ** 2 + lis[1] ** 2 < lis[2] ** 2:
        print('D')  # 钝角三角形
    elif lis[0] ** 2 + lis[1] ** 2 == lis[2] ** 2:
        print('Z')  # 直角三角形
    else:
        print('R')  # 锐角三角形
