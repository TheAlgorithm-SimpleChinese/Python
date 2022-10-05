# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 砝码问题.py
@time: 2022/10/5 23:31
"""
w = [1, 2]
n = [2, 1]

ans = set()
len_n = len(w)


def dfs(pos, value):
    if pos >= len_n:
        ans.add(value)
        return

    for i in range(n[pos] + 1):
        dfs(pos + 1, value + i * w[pos])


dfs(0, 0)
print(len(ans))
