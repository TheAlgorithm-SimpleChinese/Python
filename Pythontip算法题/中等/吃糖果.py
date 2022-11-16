# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 吃糖果.py
@time: 2022/11/16 21:21
"""
L = [5, 4, 3, 2, 1]
m = max(L)
s = sum(L) - m
if m <= s:
    print("Yes")
else:
    print("No")
