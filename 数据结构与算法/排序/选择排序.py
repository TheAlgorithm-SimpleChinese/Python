# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 选择排序.py
@time: 2022/4/27 21:11
"""
"""
算法功能：选择排序(升序)
"""


def select_sort(sortedlist):
    # 选择排序
    listlength = len(sortedlist)
    for i in range(0, listlength):  # 遍历列表
        min = i
        for j in range(i + 1, listlength):  # 遍历剩余元素
            if sortedlist[min] > sortedlist[j]:
                min = j
        # 交换元素，把选出的元素放到对应位置
        sortedlist[min], sortedlist[i] = sortedlist[i], sortedlist[min]
    return sortedlist


def main():
    lists = [3, 4, 2, 8, 9, 5, 1]  # 测试列表
    print('排序前序列为:', lists)
    print('\n排序后结果为:', select_sort(lists))


if __name__ == "__main__":
    main()
