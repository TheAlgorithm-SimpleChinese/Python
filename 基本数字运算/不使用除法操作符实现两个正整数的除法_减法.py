# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 不使用除法操作符实现两个正整数的除法_减法.py
@time: 2022/6/12 15:30
"""
"""
方法功能：计算两个自然数的除法
"""


def divide(m, n):
    print(str(m) + "除以" + str(n))
    res = 0
    remain = m
    # 被除数减除数，直到相减结果小于除数为止
    while m > n:
        m = m - n
        res += 1
    remain = m
    print("商为：" + str(res) + " 余数：" + str(remain))


def main():
    m = 14
    n = 4
    divide(m, n)


if __name__ == "__main__":
    main()
