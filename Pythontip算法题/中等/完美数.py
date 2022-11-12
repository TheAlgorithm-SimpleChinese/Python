# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 完美数.py
@time: 2022/11/12 23:50
"""
n = 3
perfects = set([1])
while True:
    tmp = set([])
    for i in perfects:
        tmp.add(i * 2)
        tmp.add(i * 3)
        tmp.add(i * 5)
    perfects.update(tmp)
    if len(perfects) > n * 3:
        break
perfects = list(perfects)
perfects.sort()
print(perfects[n - 1])
