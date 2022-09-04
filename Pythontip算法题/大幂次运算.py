# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 大幂次运算.py
@time: 2022/9/4 10:43
"""
'''
pow()方法返回 xy（x的y次方） 的值
内置的 pow() 方法
pow(x, y[, z])
函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
'''
a = 3453
n = 0
print(pow(a, n, 20132013))
