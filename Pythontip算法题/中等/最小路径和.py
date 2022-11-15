# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 最小路径和.py
@time: 2022/11/15 22:48
"""
M = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
N = M
s = M[0][0]
h = s
sh = s
for i in range(1, len(M[0])):
    h += M[0][i]
    N[0][i] = h
for j in range(1, len(M)):
    sh += M[j][0]
    N[j][0] = sh
for i in range(1, len(M)):
    for j in range(1, len(M[i])):
        N[i][j] = min(N[i - 1][j], N[i][j - 1]) + M[i][j]
print(N[-1][-1])
