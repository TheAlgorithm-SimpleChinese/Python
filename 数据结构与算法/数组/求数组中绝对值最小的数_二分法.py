# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求数组中绝对值最小的数_二分法.py
@time: 2022/5/31 21:48
"""
"""
程序功能：求数组中绝对值最小的数（升序数组）
"""


def findMin(array):
    if array is None or len(array) <= 0:
        print("输入参数不合理")
        return 0
    lens = len(array)
    # 数组中没有负数
    if array[0] >= 0:
        return array[0]
    # 数组中没有正数
    if array[lens - 1] <= 0:
        return array[lens - 1]
    begin = 0
    end = lens - 1
    # 数组中既有正数又有负数
    while True:
        mid = begin + (end - begin) // 2
        # 如果等于0，那么就是绝对值最小的数
        if array[mid] == 0:
            return 0  # 如果大于0，正负数的分界点在左侧
        elif array[mid] > 0:
            # 继续在数组的左半部分查找
            if array[mid - 1] > 0:
                end = mid - 1
            elif array[mid - 1] == 0:
                return 0
            # 找到正负数的分界点
            else:
                break  # 如果小于0，在数组右半部分查找
        else:
            # 在数组右半部分继续查找
            if array[mid + 1] < 0:
                begin = mid + 1
            elif array[mid + 1] == 0:
                return 0
            # 找到正负数的分界点
            else:
                break
    # 获取正负数分界点处绝对值最小的值
    if array[mid] > 0:
        if array[mid] < abs(array[mid - 1]):
            absMin = array[mid]
        else:
            absMin = array[mid - 1]
    else:
        if abs(array[mid]) < array[mid + 1]:
            absMin = array[mid]
        else:
            absMin = array[mid + 1]
    return absMin


def main():
    arr = [-10, -5, -2, 7, 15, 50]
    print("绝对值最小的数为：" + str(findMin(arr)))


if __name__ == "__main__":
    main()
