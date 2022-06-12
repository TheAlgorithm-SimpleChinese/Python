# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 不用加减乘除运算实现减法.py
@time: 2022/6/12 16:24
"""
"""
方法功能：不使用加减乘除运算实现减法（位运算）
"""


def add(n1, n2):
    sums = 0  # 保存不进位相加结果
    carry = 0  # 保存进位值
    while True:  # 判断进位值是否为0
        sums = n1 ^ n2  # 异或代替不进位相加
        carry = (n1 & n2) << 1  # 与操作代替计算进位值
        n1 = sums
        n2 = carry
        if carry == 0:
            break
    return sums


def sub(a, b):
    return add(a, add(~b, 1))

def main():
    print(sub(2, 4))


if __name__ == "__main__":
    main()
