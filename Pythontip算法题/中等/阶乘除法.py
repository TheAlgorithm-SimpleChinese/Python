# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 阶乘除法.py
@time: 2022/11/13 22:18
"""

k = 72


# k等于(m+1) * (m+2)*...*n
def Chen(m, n):
    res = 1
    for i in range(m + 1, n + 1):
        res *= i
    return res


m = 1
flag = 0
n = 0
while not flag:
    n = m + 1
    res = Chen(m, n)
    while res <= k:
        if res == k:
            flag = 1
            break
        else:
            n += 1
            res = Chen(m, n)
    m += 1  # 最后m还会加一，所有输出时要m-1
print(n, m - 1)
