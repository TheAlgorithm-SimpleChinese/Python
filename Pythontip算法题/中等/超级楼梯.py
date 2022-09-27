# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 超级楼梯.py
@time: 2022/9/27 22:39
"""


def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return f(n - 1) + f(n - 2)


n = 3
print(f(n))
