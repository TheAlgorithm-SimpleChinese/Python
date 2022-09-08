# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 信息加密.py
@time: 2022/8/9 13:54
"""
a = "cagy"
b = 3
for i in a:
    y = ord(i) + b
    if ord(i) + b > 123:
        y = ((ord(i) + b) % 123) + 97
    print(chr(y), end="")
