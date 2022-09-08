# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 相同数字.py
@time: 2022/8/23 16:51
"""
L = [123, 432, 23]
print("YES" if len(L) != len(set(L)) else "NO")
