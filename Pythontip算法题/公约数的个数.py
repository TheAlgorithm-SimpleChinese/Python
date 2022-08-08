# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 公约数的个数.py
@time: 2022/8/8 14:39
"""
a = 24
b = 36
cnt = 0
if a > b:
    m, n = a, b
else:
    m, n = b, a
for i in range(1, n + 1):
    if m % i == 0 and n % i == 0:
        cnt += 1
print(cnt)
