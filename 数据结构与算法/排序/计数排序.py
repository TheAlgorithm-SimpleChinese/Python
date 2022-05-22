# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 计数排序.py
@time: 2022/4/29 22:52
"""
"""
算法功能：计数排序
"""


def counting_sort(arr):
    if len(arr) <= 1:
        return arr

    maxVal = max(arr)
    countArr = [0 for _ in range(maxVal + 1)]
    for i in arr:
        countArr[i] += 1
    for i in range(1, len(countArr)):
        countArr[i] += countArr[i - 1]
    res = [0 for _ in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        res[countArr[arr[i]] - 1] = arr[i]
        countArr[arr[i]] -= 1
        # 必须要减1，由于待排序元素在res中的位置是由计数数组的值来决定的。
        # 当遍历了元素x之后，小于x的元素不会受影响，大于x的元素不会受影响，
        # 只有等于x的元素会受影响，在往res中压的时候，要比x的位置往前移动一位，
        # 因此需要将计数数组中的下标为x的值减1，使得下次在遍历到x的时候，
        # 压入的位置在前一个x的位置之前
    return res


def main():
    list = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为：", list)
    print("排序后序列为：", counting_sort(list))


if __name__ == '__main__':
    main()
