# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 乘法运算.py
@time: 2022/10/12 22:02
"""
a = 2
b = 2
n = m = 8  # n为每一行显示的字符总长度，m为进位后的一行总长度
y = b
print('%*d' % (n, a))  # 打印a，行的总长度为n
print('x%*d' % (n - 1, b))  # 打印x, 再打印b，b的总长度为n - 1
if y > 9:  # 乘数为两位数时，需要输出过程
    print('-' * n)
    while y > 0:
        t, y = y % 10, y // 10
        print('%*d' % (m, t * a))
        m -= 1  # m - 1后，作为下一行的总长度
print('-' * n)
print('%*d' % (n, a * b))
print('*' * 20)
