# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 找出数组中丢失的数_异或法.py
@time: 2022/5/22 23:12
"""
"""
要求描述：给定一个由n-1个整数数组组成的未排列的数组序列，其元素都是1到n中的不同的整数，请写出一个
寻找数组序列中缺失整数的线性时间算法
"""
"""
程序功能：找出数组中丢失的数
"""


def getNum(arr):
    if arr is None or len(arr) <= 0:
        print("参数不合理")
        return -1
    a = arr[0]
    b = 1
    lens = len(arr)
    i = 1
    while i < lens:
        a = a ^ arr[i]
        i += 1
    i = 2
    while i <= lens + 1:
        b = b ^ i
        i += 1
    return a ^ b


def main():
    arr = [1, 4, 3, 2, 7, 5]
    print(getNum(arr))


if __name__ == "__main__":
    main()
