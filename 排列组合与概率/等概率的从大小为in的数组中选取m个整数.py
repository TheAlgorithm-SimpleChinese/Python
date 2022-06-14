# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 等概率的从大小为in的数组中选取m个整数.py
@time: 2022/6/14 16:12
"""
import random


def getRandomM(a, n, m):
    if a is None or n <= 0 or n < m:
        print("参数不合理")
        return
    i = 0
    while i < m:
        j = random.randint(i, n - 1)  # // 获取i到n-1间的随机数
        # 随机选出的元素放到数组的前面
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        i += 1


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    m = 6  # 随机选出6个数
    getRandomM(a, n, m)
    i = 0
    while i < m:
        print(a[i])
        i += 1


if __name__ == "__main__":
    main()
