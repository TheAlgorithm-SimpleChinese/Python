# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 整数解.py
@time: 2022/9/23 22:46
"""
a = 9
b = 15
flag = "No"
if b == 0:
    flag = "yes"
else:
    for x in range(-10000, abs(a) + 1):  # x最大值不会超过a的绝对值
        if b == x * (a - x):
            flag = "Yes"
            break
print(flag)
