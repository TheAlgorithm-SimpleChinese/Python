# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个数是否为2的n次方_构造法.py
@time: 2022/6/5 20:25
"""
""""
判断n能否表示成2的n次方 
"""


def isPower(n):
    if n < 1:
        return False
    i = 1
    while i <= n:
        if i == n:
            return True
        i <<= 1  # 移位等于，类似于+=
    return False


def main():
    if isPower(8):
        print("8能表示成2的n次方")
    else:
        print("8不能表示成2的n次方")
    if isPower(9):
        print("9能表示成2的n次方")
    else:
        print("9不能表示成2的n次方")


if __name__ == "__main__":
    main()
