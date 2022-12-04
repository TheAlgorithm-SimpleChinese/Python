# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 特殊的9位数.py
@time: 2022/12/4 19:11
"""
a = 0


def solve_it():
    global a

    def shu(k, m):
        global a
        if k == 9:
            a = m
            return
        for i in range(1, 10):
            if str(i) not in str(m) and (m * 10 + i) % (k + 1) == 0:
                shu(k + 1, m * 10 + i)

    shu(0, 0)
    return a  # your answer


print(solve_it())  # 答案需要输出
