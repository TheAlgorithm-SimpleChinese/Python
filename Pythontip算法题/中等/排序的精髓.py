# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 排序的精髓.py
@time: 2022/10/24 17:01
"""
L = [2, 8, 0, 3]
count = 0
lens = len(L)
for i in range(lens - 1):
    for j in range(lens - i - 1):
        if L[j] > L[j + 1]:
            count += 1
            L[j + 1], L[j] = L[j], L[j + 1]
print(count)
