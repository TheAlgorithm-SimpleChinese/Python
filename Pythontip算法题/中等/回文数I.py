# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 回文数I.py
@time: 2022/10/20 19:25
"""
M = 78


def solve_it(m):
    for step in range(1, 8):
        if m == int(str(m)[::-1]):
            return step - 1
        else:
            m += int(str(m)[::-1])
    else:
        return 0


print(solve_it(M))
