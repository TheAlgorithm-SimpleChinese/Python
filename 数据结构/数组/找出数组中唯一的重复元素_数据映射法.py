# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 找出数组中唯一的重复元素_数据映射法.py
@time: 2022/4/24 20:18
"""
"""
要求描述：数字1~1000放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，
设计算法，找出重复元素
"""


def findDup(array):
    if array is None:
        return -1
    lens = len(array)
    index = 0
    i = 0
    while True:
        # 数组中的元素的值只能小于len，否则会越界
        if array[i] >= lens:
            return -1
        if array[index] < 0:
            break
        # 访问过，通过变相反数的方法进行标记
        array[index] *= -1
        # index的后继为array[index]
        index = -1 * array[index]
        if index >= lens:
            print("数组中有非法数字")
            return -1
    return index


def main():
    array = [1, 3, 4, 2, 5, 3]
    print(findDup(array))


if __name__ == "__main__":
    main()
