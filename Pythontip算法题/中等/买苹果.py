# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 买苹果.py
@time: 2022/10/19 22:48
"""
N = 3
M = 1
print(0 if N % M == 0 else (int(N / M) + 1) * M - N)
