# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 希尔排序.py
@time: 2022/4/27 21:12
"""


# 希尔排序(Shell Sort)
def shell_sort(arr):
    length = len(arr)  # 数组的长度
    gap = length // 2  # 选择增量为length/2,
    while gap > 0:
        for i in range(gap, length):  # 排序每一组
            temp = arr[i]
            preIndex = i - gap
            while preIndex >= 0 and arr[preIndex] > temp:  # 交换排序
                arr[preIndex + gap] = arr[preIndex]
                preIndex -= gap
            arr[preIndex + gap] = temp
        gap //= 2  # 持续缩小增量
    return arr
