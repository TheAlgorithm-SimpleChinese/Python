# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个自然数是否是某个数的平方_直接计算法.py
@time: 2022/6/5 20:24
"""
"""
程序功能：判断一个自然数是否是某个数的平方
"""


def isPower(n):
    if n <= 0:
        print(n + "不是自然数")
        return False
    i = 1
    while i < n:
        m = i * i
        if m == n:
            return True
        elif m > n:
            return False
        i += 1
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
