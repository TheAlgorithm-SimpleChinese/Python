# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断还有几盏灯泡亮着.py
@time: 2022/6/15 14:24
"""
"""
100个灯泡排成一排，第一轮将所有灯泡打开；第二轮每隔一个灯泡关掉一个，即排在偶数的灯泡被关掉，
第三轮每隔两个灯泡，将开着的灯泡关掉，关掉的灯泡打开。依次类推，第100轮结束的时候，还有几盏灯泡亮着？
"""


def factorIsOdd(a):
    total = 0
    i = 1
    while i <= a:
        if a % i == 0:
            total += 1
        i += 1
    if total % 2 == 1:
        return 1
    else:
        return 0


def totalCount(num, n):
    count = 0
    i = 0
    while i < n:
        # //判断因子数是否为奇数，如果是奇数（灯亮），那么加1
        if factorIsOdd(num[i]) == 1:
            print("亮着的灯的编号是：" + str(num[i]))
            count += 1
        i += 1
    return count


def main():
    num = [None] * 100
    i = 0
    while i < 100:
        num[i] = i + 1
        i += 1
    count = totalCount(num, 100)
    print("最后总共有" + str(count) + "盏灯亮着。")


if __name__ == "__main__":
    main()
