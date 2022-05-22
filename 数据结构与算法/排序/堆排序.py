# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 堆排序.py
@time: 2022/4/27 21:12
"""
"""
算法功能：堆排序
"""


# 堆排序 (Heap sort )
def heap_sort(arr):
    length = len(arr) - 1  # 获取序列元素个数
    first_sort_count = length // 2
    for i in range(first_sort_count):  # 把序列调整为大顶堆
        heap_adjust(arr, first_sort_count - i, length)

    for i in range(length - 1):
        arr = swap_param(arr, 1, length - i)  # 把堆顶元素和堆末尾的元素交换，然后把剩下的元素调整为一个大根堆
        heap_adjust(arr, 1, length - i - 1)

    return [arr[i] for i in range(1, len(arr))]


def heap_adjust(arr, start, end):
    temp = arr[start]

    i = start
    j = 2 * i
    while j <= end:
        if j < end and arr[j] < arr[j + 1]:
            j += 1
        if temp < arr[j]:
            arr[i] = arr[j]
            i = j
            j = 2 * i
        else:
            break
    arr[i] = temp


def swap_param(arr, i, j):  # 交换堆顶和堆底节点
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    list = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为：", list)
    list.insert(0, 0)  # 此处0用来占位，使得序列的下标从1开始
    print("排序后序列为：", heap_sort(list))


if __name__ == '__main__':
    main()
