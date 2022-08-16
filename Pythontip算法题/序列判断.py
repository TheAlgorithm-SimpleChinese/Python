# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 序列判断.py
@time: 2022/8/14 19:39
"""
L = [1, 1, 3, 3, 4]
i = 0
j = 0
while (i < len(L) - 1) and (j < len(L) - 1):
    if L[i] <= L[i+1]:
        i += 1
    if L[j] >= L[j+1]:
        j += 1

if i == len(L) - 1:
    print("UP")
elif j == len(L) - 1:
    print("DOWN")
else:
    print("WRONG")

