# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 找出数组中丢失的数_累加求和法.py
@time: 2022/5/22 23:05
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
    suma = 0
    sumb = 0
    i = 0
    while i < len(arr):
        suma = suma + arr[i]
        sumb = sumb + i
        i += 1
    sumb = sumb + len(arr) + len(arr) + 1
    return sumb - suma


def main():
    arr = [1, 4, 3, 2, 7, 5]
    print(getNum(arr))


if __name__ == "__main__":
    main()
