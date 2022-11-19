# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 幸运树.py
@time: 2022/11/19 23:15
"""
import itertools

L = [[1, 2, 4], [3, 1, 2], [1, 4, 7]]


def is_lucky_number(num):
    for i in str(num):
        if i != '4' and i != '7':
            return False
    return True


contain_lucky_edge = []

n = len(L) + 1  # 求出题目中的n，树的节点数等于边数+1
path = [[0 for _ in range(n)] for _ in range(n)]
for u, v, p in L:
    path[u - 1][v - 1] = path[v - 1][u - 1] = 1
    if is_lucky_number(p):
        contain_lucky_edge.append((u, v))
        contain_lucky_edge.append((v, u))
for i in range(n):
    for j, m in itertools.combinations(range(n), 2):
        if path[j][m] == 1:  # 表示j和m节点已经连通
            continue
        if path[i][j] == 1 and path[i][m] == 1:  # 表示j和m节点可以通过i连通
            path[j][m] = path[m][j] = 1
            if (i + 1, j + 1) in contain_lucky_edge or (i + 1, m + 1) in contain_lucky_edge:
                contain_lucky_edge.append((j + 1, m + 1))
                contain_lucky_edge.append((m + 1, j + 1))
cnt = 0
for a, b, c in itertools.permutations(range(1, n + 1), 3):
    if (a, b) in contain_lucky_edge and (b, c) in contain_lucky_edge:
        cnt += 1
print(cnt)
