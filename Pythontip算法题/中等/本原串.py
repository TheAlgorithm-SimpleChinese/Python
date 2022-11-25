# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 本原串.py
@time: 2022/11/25 22:58
"""
n = 1


def f(n):
    if n == 1:
        return 2
    all = pow(2, n, 2017)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            all -= f(i)
            if all < 0:
                all += 2017
    return all % 2017


print(f(n))
