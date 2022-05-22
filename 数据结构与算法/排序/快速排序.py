# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 快速排序.py
@time: 2022/4/27 21:12
"""
"""
算法功能：快速排序(升序)
"""


def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:  # 如果只有一个元素或者参数有误，返回列表
        return lists
    key = lists[left]  # 以为第一个元素为基准数并记录
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:  # 从尾部开始扫描（小的数放在基准数的左边）
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:  # 从头部开始扫描（大的数放在基准数右边）
            left += 1
        lists[right] = lists[left]
    lists[right] = key  # 基准数放在合适位置
    quick_sort(lists, low, left - 1)  # 递归排序
    quick_sort(lists, left + 1, high)
    return lists


def main():
    lists = [3, 4, 2, 8, 9, 5, 1]  # 测试列表
    print('排序前序列为:', lists)
    print('\n排序后结果为:', quick_sort(lists, 0, len(lists) - 1))


if __name__ == "__main__":
    main()
