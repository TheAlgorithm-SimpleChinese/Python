# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 用一个随机函数得到另一个随机函数.py
@time: 2022/6/14 16:20
"""
import random


# 返回0和1的概率都为1/2
def func1():
    return int(round(random.random()))


# 返回0的概率为1/4,返回1的概率为3/4
def func2():
    a1 = func1()
    a2 = func1()
    tmp = a1
    tmp |= (a2 << 1)
    if tmp == 0:
        return 0
    else:
        return 1


def main():
    i = 0
    while i < 16:
        print(func2())
        i += 1
    print('\n')
    i = 0
    while i < 16:
        print(func2())
        i += 1


if __name__ == "__main__":
    main()
