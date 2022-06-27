# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 最小公倍数.py
@time: 2022/6/27 16:28
"""
a = 3
b = 5
print([x for x in range(max(a, b), a * b + 1) if not x % a and not x % b][0])
