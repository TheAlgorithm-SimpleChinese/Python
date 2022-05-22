# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 希尔排序.py
@time: 2022/4/27 21:12
"""
"""
算法功能：希尔排序
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


def main():
    list = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为：", list)
    print("排序后序列为：", shell_sort(list))


if __name__ == '__main__':
    main()
