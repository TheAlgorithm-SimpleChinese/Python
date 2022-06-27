# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求中位数.py
@time: 2022/6/27 16:27
"""
L = [0, 1, 2, 3, 4]
L.sort()
if len(L) % 2 == 0:
    print(round((L[int(len(L) / 2 - 1)] + L[int(len(L) / 2)]) / 2, 1))
else:
    print(round(L[int(len(L) / 2)], 1))
