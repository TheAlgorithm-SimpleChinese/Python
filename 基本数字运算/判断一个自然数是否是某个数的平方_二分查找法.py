# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个自然数是否是某个数的平方_二分查找法.py
@time: 2022/6/5 20:27
"""
"""
程序功能：判断一个自然数是否是某个数的平方
"""


def isPower(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        power = mid * mid
        # 接着在1～(mid-1)区间查找
        if power > n:
            high = mid - 1
        # 接着在mid+1到n区间内查找
        elif power < n:
            low = mid + 1
        else:
            return True
    return False


def main():
    n1 = 15
    n2 = 16
    if isPower(n1):
        print(str(n1) + "是某个自然数的平方")
    else:
        print(str(n1) + "不是某个自然数的平方")
    if isPower(n2):
        print(str(n2) + "是某个自然数的平方")
    else:
        print(str(n2) + "不是某个自然数的平方")


if __name__ == "__main__":
    main()
