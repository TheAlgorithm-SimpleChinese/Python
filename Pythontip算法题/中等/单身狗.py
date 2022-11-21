# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 单身狗.py
@time: 2022/11/21 22:07
"""
from functools import reduce

L = [1, 1, 4, 4, 3, 5, 5]
print(reduce(lambda x, y: x ^ y, L))
