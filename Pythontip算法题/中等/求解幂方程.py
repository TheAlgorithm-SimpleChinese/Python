# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求解幂方程.py
@time: 2022/11/23 21:26
"""
import math

y = float(input())
eps = 0.00000000001
l = 0
r = 11
while float(r) - float(l) >= eps:
    mid = (l + r) * 0.5
    if pow(mid, mid) < y:
        l = mid
    else:
        r = mid
print("%.3f" % l)
