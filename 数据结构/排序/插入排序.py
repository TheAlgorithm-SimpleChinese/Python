# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 插入排序.py
@time: 2022/4/27 21:11
"""
"""
算法功能：插入排序(升序)
"""


def insert_sort(sortedlist):
    # 插入排序
    listlength = len(sortedlist)  # 序列长度
    for i in range(1, listlength):  # 从第二个元素开始遍历
        key = sortedlist[i]  # 标记当前需要进行插入操作的元素
        j = i - 1
        while j >= 0:  # 找出合适地插入位置
            if sortedlist[j] > key:
                sortedlist[j + 1] = sortedlist[j]  # 元素移位
                sortedlist[j] = key
            j -= 1
    return sortedlist


def main():
    lists = [3, 4, 2, 8, 9, 5, 1]  # 测试列表
    print('排序前序列为:')
    for i in lists:
        print(i, end=" ")
    print('\n排序后结果为:')
    for i in (insert_sort(lists)):
        print(i, end=" ")


if __name__ == "__main__":
    main()
