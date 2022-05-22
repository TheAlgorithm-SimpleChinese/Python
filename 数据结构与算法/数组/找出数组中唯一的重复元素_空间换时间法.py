# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 找出数组中唯一的重复元素_空间换时间法.py
@time: 2022/4/24 19:32
"""
"""
要求描述：数字1~1000放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，
设计算法，找出重复元素
"""
"""
方法功能：在数组中找唯一重复的元素（使用字典辅助）
输入参数：array:数组对象的引用
 返回值：重复元素的值，如果无重复元素则返回-1
"""


# 使用字典
def findDup(array):
    if array is None:
        return -1
    lens = len(array)
    hashTable = dict()  # 创建空字典
    i = 0
    while i < lens - 1:  # 初始化字典
        hashTable[i] = 0
        i += 1
    j = 0
    while j < lens:  # 把数组元素映射为字典的键
        if hashTable[array[j] - 1] == 0:
            hashTable[array[j] - 1] = array[j] - 1
        else:
            return array[i]
        j += 1
    return -1


def main():
    array = [1, 3, 4, 2, 5, 3]
    print(findDup(array))


if __name__ == "__main__":
    main()
