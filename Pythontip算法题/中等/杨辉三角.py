# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 杨辉三角.py
@time: 2022/9/25 23:04
"""
n = 6
m = []
for i in range(n):
    m.append([])
    for j in range(i + 1):
        m[i].append(0)
        if j == 0 or j == i:
            m[i][j] = str(1)
        else:
            temp = int(m[i - 1][j - 1]) + int(m[i - 1][j])
            m[i][j] = str(temp)
for i in range(len(m)):
    for j in range(len(m[i])):
        if j == len(m[i]) - 1:
            print(m[i][j])
        else:
            print(m[i][j], end=' ')
