# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 密码生成.py
@time: 2022/9/5 23:03
"""
a = 1
b = 2
x = 1
y = 4
a = (a * pow(10, x - 1)) % b
r = ''
# 将a扩大10^(x-1)倍，此时a/b算出的数的小数位第i位，即原a/b的小数第x+i位。
for i in range(y - x + 1):
    a = (a % b) * 10
    r += str(a // b)
print(r)
