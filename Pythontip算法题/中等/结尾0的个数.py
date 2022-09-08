# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 结尾0的个数.py
@time: 2022/7/5 16:39
"""
L = [4, 2, 25, 7777777, 100, 3, 77777777, 77777777, 77777777, 77777777]
c2 = 0  # 2的因数个数
c5 = 0  # 5的因数个数
d = 0
for i in range(0, len(L)):
    b = L[i]
    while b % 2 == 0:
        c2 += 1
        b = b // 2
    while b % 5 == 0:
        c5 += 1
        b = b // 5
    if c2 >= c5:
        d = c5  # 两者取小
    else:
        d = c2
print(d)
