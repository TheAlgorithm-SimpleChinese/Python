# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 输出字符串奇数位置的字符串.py
@time: 2022/6/27 16:24
"""
a = 'xyzwd'
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end="")
