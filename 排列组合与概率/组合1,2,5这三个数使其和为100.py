# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 组合1,2,5这三个数使其和为100.py
@time: 2022/6/15 14:19
"""
"""
求出用1，2，5这三个数不同个数组合的和为100的组合个数。为了更好地理解题目的意思，
下面给出几组可能的组合：100个1，0个2和0个5，它们的和为100；50个1，25个2，0个5的和也是100；50个1，20个2，2个5的和也为100。
"""


def combinationCount(n):
    count = 0
    num1 = n  # 1最多的个数
    num2 = n / 2  # 2最多的个数
    num5 = n / 5  # 5最多的个数
    x = 0
    while x <= num1:
        y = 0
        while y <= num2:
            z = 0
            while z <= num5:
                if x + 2 * y + 5 * z == n:  # 满足条件
                    count += 1
                z += 1
            y += 1
        x += 1
    return count


def main():
    print(combinationCount(100))


if __name__ == "__main__":
    main()
