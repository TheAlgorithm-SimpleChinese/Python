# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 找出数组中唯一的重复元素_异或法.py
@time: 2022/4/24 19:56
"""
"""
要求描述：数字1~1000放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，
设计算法，找出重复元素
"""


def findDup(array):
    if array is None:
        return -1
    lens = len(array)
    result = 0
    i = 0
    while i < lens:  # 对数组元素逐一异或
        result ^= array[i]
        i += 1
    j = 1
    while j < lens:
        result ^= j
        j += 1
    return result


def main():
    array = [1, 3, 4, 2, 5, 3]
    print(findDup(array))


if __name__ == "__main__":
    main()
