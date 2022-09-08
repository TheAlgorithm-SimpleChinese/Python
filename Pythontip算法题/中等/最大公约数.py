# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 最大公约数.py
@time: 2022/6/27 16:27
"""
a = 3
b = 5


def gy(n):
    return [x for x in range(1, n + 1) if n % x == 0]


print(max([i for i in gy(a) for j in gy(b) if i == j]))
