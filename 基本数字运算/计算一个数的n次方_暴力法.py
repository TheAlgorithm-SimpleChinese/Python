# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 计算一个数的n次方_暴力法.py
@time: 2022/6/14 16:34
"""
"""
方法功能：计算一个数的n次方
输入参数：d为底数，n为幂
返回值：  d^n
"""


def power(d, n):
    if n == 0:
        return 1
    if n == 1:
        return d
    result = 1.0
    if n > 0:
        i = 1
        while i <= n:
            result *= d
            i += 1
        return result
    else:
        i = 1
        while i <= abs(n):
            result = result / d
            i += 1
    return result


def main():
    print(power(2, 3))
    print(power(-2, 3))
    print(power(2, -3))


if __name__ == "__main__":
    main()
