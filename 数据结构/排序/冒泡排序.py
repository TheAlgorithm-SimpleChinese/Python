# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 冒泡排序.py
@time: 2022/4/27 21:11
"""
"""
算法功能：冒泡排序(升序)
"""


def bubble_sort(sortedlist):
    for i in range(len(sortedlist) - 1):  # 遍历需要排序的元素
        for j in range(len(sortedlist) - i - 1):  # 遍历剩余未排序元素
            if sortedlist[j] > sortedlist[j + 1]:
                sortedlist[j], sortedlist[j + 1] = sortedlist[j + 1], sortedlist[j]  # 交换位置
    return sortedlist


def main():
    lists = [3, 4, 2, 8, 9, 5, 1]  # 测试列表
    print('排序前序列为:')
    for i in lists:
        print(i, end=" ")
    print('\n排序后结果为:')
    for i in (bubble_sort(lists)):
        print(i, end=" ")


if __name__ == "__main__":
    main()
