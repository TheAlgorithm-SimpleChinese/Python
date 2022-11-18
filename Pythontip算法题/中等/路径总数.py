# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 路径总数.py
@time: 2022/11/18 21:38
"""
m = 3
n = 4
x = 2
y = 3


# 总共走了m+n-2步，其中向左m-1步，使用排列组合公式就行了
def An(num):
    n = 1
    for i in range(1, num + 1):
        n *= i
    return n


def C(m, n):
    return An(n) // An(m) // An(n - m)


m, n, x, y = m - 1, n - 1, x - 1, y - 1
print(C(m, m + n) - C(x, x + y) * C(m - x, m + n - x - y))
