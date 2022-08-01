# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 结尾非零数的奇偶性.py
@time: 2022/8/1 15:38
"""

L = [2, 8, 3, 50]
a = 0
d = 0
for c in L:
    while c % 2 == 0:
        c = c / 2
        a += 1
    while c % 5 == 0:
        c = c / 5
        a -= 1
    if c % 2 == 0:
        d += 1
if d + a > 0:
    print(0)
else:
    print(1)
