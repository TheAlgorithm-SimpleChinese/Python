# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求解100以内的所有素数.py
@time: 2022/6/27 16:25
"""
print(" ".join("%s" % x for x in range(2, 100) if not [y for y in range(2, x) if x % y == 0]))
