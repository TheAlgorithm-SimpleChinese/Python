# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 回文子串.py
@time: 2022/8/10 15:30
"""
a = "abcba"
n = 5
flag = False  # 标识
c = []
for i in range(len(a)):
    if i + n <= len(a):  # 判断是否取完
        c = a[i:i + n]
    if c == c[-1::-1]:
        flag = True
if flag:
    print('YES')
else:
    print('NO')
