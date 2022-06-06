# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个自然数是否是某个数的平方_减法运算法.py
@time: 2022/6/5 20:28
"""
"""
程序功能：判断一个自然数是否是某个数的平方
"""


def isPower(n):
    minus = 1
    while n > 0:
        n = n - minus
        # n是某个数的平方
        if n == 0:
            return True
        # n不是某个数的平方
        elif n < 0:
            return False
        # 每次减数都加2
        else:
            minus += 2
    return False


def main():
    n1 = 15
    n2 = 16
    if isPower(n1):
        print(str(n1) + "是某个自然数的平方")
    else:
        print(str(n1) + "不是某个自然数的平方")
    if isPower(n2):
        print(str(n2) + "是某个自然数的平方")
    else:
        print(str(n2) + "不是某个自然数的平方")


if __name__ == "__main__":
    main()
