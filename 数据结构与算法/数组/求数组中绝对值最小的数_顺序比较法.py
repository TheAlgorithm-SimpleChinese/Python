# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求数组中绝对值最小的数_顺序比较法.py
@time: 2022/5/31 21:42
"""
"""
程序功能：求数组中绝对值最小的数（升序数组）
"""


def findMin(array):
    if array is None or len(array) <= 0:
        print("输入参数不合理")
        return 0
    mins = 2 ** 32
    i = 0
    while i < len(array):
        if abs(array[i]) < abs(mins):
            mins = array[i]
        i += 1
    return mins


def main():
    arr = [-10, -5, -2, 7, 15, 50]
    print("绝对值最小的数为：" + str(findMin(arr)))


if __name__ == "__main__":
    main()
