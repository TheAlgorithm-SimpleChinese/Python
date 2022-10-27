# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 圆的面积.py
@time: 2022/10/27 22:00
"""
from math import *

x1 = 20.0
y1 = 30.0
r1 = 15.0
x2 = 40.0
y2 = 30.0
r2 = 30.0
d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if r1 > r2:
    r1, r2 = r2, r1
if d >= r1 + r2:
    Area = 0
elif r2 - r1 >= d:
    Area = pi * r1 * r1
else:
    ang1 = acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
    ang2 = acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
    Area = ang1 * r1 * r1 + ang2 * r2 * r2 - r1 * d * sin(ang1)

print('%.3f' % Area)
