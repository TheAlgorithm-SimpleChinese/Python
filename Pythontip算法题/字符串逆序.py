# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 字符串逆序.py
@time: 2022/6/22 14:39
"""
a = "Good"
temp = reversed(list(a))
s = ""
for i in temp:
    s += i
print(s)
