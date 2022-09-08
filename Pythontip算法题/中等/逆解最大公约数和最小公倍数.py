# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 逆解最大公约数和最小公倍数.py
@time: 2022/8/8 15:03
"""
a = 3
b = 60
c = []
d = []
e = []
for i in range(b):
    for j in range(b):
        if i * j == b * a:
            for m in range(i, 0, -1):
                if i % m == 0 and b % m == 0:
                    if m == a:
                        c.append(i)
                        d.append(j)
for n in range(len(c)):
    e.append(c[n] + d[n])
f = min(e)
g = e.index(f)
print(c[g], d[g])
