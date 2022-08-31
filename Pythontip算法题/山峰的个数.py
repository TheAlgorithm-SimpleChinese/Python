# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 山峰的个数.py
@time: 2022/8/31 21:24
"""
h = [0.9, 1.2, 1.22, 1.1, 1.6, 0.99]
sum = 0
for i in range(len(h) - 2):
    if (h[i + 1] > h[i]) and (h[i + 1] > h[i + 2]):
        sum += 1
print(sum)
