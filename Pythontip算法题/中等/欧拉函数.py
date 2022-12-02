# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 欧拉函数.py
@time: 2022/12/2 22:51
"""
n = 10


def gys(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m


cnt = 1
for i in range(2, n):
    if gys(i, n) == 1:
        cnt = cnt + 1
print(cnt)
