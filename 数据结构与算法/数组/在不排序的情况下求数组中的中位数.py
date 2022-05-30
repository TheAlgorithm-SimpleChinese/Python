# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 在不排序的情况下求数组中的中位数.py
@time: 2022/5/30 22:49
"""
"""
程序功能：在不排序的情况下求数组中的中位数
"""


class Test:
    def __init__(self, pos=0):
        self.pos = pos

    # 以arr[low]为基准把数组分成两部分
    def partition(self, arr, low, high):
        key = arr[low]
        while low < high:
            while low < high and arr[high] > key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < key:
                low += 1
            arr[high] = arr[low]
        arr[low] = key
        self.pos = low

    def getMid(self, arr):
        low = 0
        n = len(arr)
        high = n - 1
        mid = (low + high) // 2
        while True:
            # 以arr[low]为基准把数组分成两部分
            self.partition(arr, low, high)
            if self.pos == mid:  # 找到中位数
                break
            elif self.pos > mid:  # 继续在右半部分查找
                high = self.pos - 1
            else:  # 继续在左半部分查找
                low = self.pos + 1
        # 如果数组长度是奇数，中位数为中间的元素，否则就是中间两个数的平均值
        return arr[mid] if (n % 2) != 0 else (arr[mid] + arr[mid + 1]) // 2


def main():
    arr = [7, 5, 3, 1, 11, 9]
    print(Test().getMid(arr))


if __name__ == "__main__":
    main()
