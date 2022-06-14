# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 计算一个数的n次方_递归法.py
@time: 2022/6/14 16:35
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
    tmp = power(d, abs(n) // 2) + 0.0
    # print  tmp
    if n > 0:
        if n % 2 == 1:  # n为奇数
            return tmp * tmp * d
        else:  # n为偶数
            return tmp * tmp
    else:
        if n % 2 == 1:
            return 1 / (tmp * tmp * d)
        else:
            return 1 / (tmp * tmp)


def main():
    print(power(2, 3))
    print(power(-2, 3))
    print(power(2, -3))


if __name__ == "__main__":
    main()
