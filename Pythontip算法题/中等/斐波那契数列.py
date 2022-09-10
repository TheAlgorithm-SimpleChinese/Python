# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 斐波那契数列.py
@time: 2022/9/10 10:28
"""
n = 2
a = 1
b = 1
count = 0
while True:
    if n == 1 or n == 2:
        c = 1
        break
    c = a + b
    a = b
    b = c
    count += 1
    if count == n - 2:  # 循环次数等于 = 第n项值 - 2
        break
print(c % 20132013)
