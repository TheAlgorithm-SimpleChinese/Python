# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 365or366.py
@time: 2022/8/10 16:08
"""
year = "2008"
y = int(year)
if y % 4 == 0 and y % 100 != 0:
    print(366)
elif y % 400 == 0:
    print(366)
else:
    print(365)
