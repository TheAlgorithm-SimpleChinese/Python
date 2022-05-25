# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 找出数组中出现奇数次的数_异或法.py
@time: 2022/5/25 20:18
"""
"""
题目描述：数组中有N+2个数，其中，N个数出现偶数次，2个数出现奇数次，两个数不相等，请用O（1）的时间复杂度
找出这两个数。不需要位置，只需找出这两个数。
"""
"""
程序功能：找出数组中出现奇数次的数
"""


def get2Num(arr):
    if arr is None or len(arr) < 1:
        print("参数不合理")
        return
    result = 0
    position = 0
    # 计算数组中所有数字异或的结果
    i = 0
    while i < len(arr):
        result = result ^ arr[i]
        i += 1
    tmpResult = result  # 临时保存异或结果
    # 找出异或结果中其中一个位值为1的位数(如1100，位值为1位数为2和3)
    i = result
    while i & 1 == 0:
        position += 1
        i = i >> 1
    i = 1
    while i < len(arr):
        # 异或的结果与所有第position位为1的数异或，结果一定是出现一次的两个数中其中一个
        if ((arr[i] >> position) & 1) == 1:
            result = result ^ arr[i]
        i += 1
    print(result)
    # 得到另外一个出现一次的数
    print(result ^ tmpResult)


def main():
    arr = [3, 5, 6, 6, 5, 7, 2, 2]
    get2Num(arr)


if __name__ == "__main__":
    main()
