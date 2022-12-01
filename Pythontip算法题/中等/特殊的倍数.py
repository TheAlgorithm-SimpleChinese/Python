# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 特殊的倍数.py
@time: 2022/12/1 23:31
"""
n = 1
b = 1
m = 1
while b % n != 0:
    m += 1
    b = int(bin(m)[2:])
print(b)
