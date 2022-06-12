# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 不使用除法操作符实现两个正整数的除法_移位法.py
@time: 2022/6/12 15:38
"""
"""
方法功能：计算两个自然数的除法
"""


def divide(m, n):
    print(str(m) + "除以" + str(n))
    result = 0
    while m >= n:
        multi = 1
        # multi * n>m/2(即2* multi * n >m)时结束循环
        while multi * n <= (m >> 1):
            multi <<= 1
        result += multi
        # 相减的结果进入下次循环
        m -= multi * n
    print("商为：" + str(result) + " 余数：" + str(m))


def main():
    m = 14
    n = 4
    divide(m, n)


if __name__ == "__main__":
    main()
