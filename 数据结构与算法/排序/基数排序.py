# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 基数排序.py
@time: 2022/4/27 21:12
"""
"""
算法功能：基数排序
"""


# 基数排序(Cardinality Sorting)
def get_bite(num, i):  # 获取元素第i位的数
    return (num % (i * 10) - (num % i)) // i


def getMax(numList):  # 获取数组中的最大值
    if len(numList) == 1:
        return numList[0]
    maxNum = numList[0]
    for i in range(len(numList)):
        if numList[i] > maxNum:
            maxNum = numList[i]
    return maxNum


def cardinality_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    maxNum = getMax(arr)
    bitCount = 0
    index = 1
    while maxNum // index:
        bitCount += 1
        index *= 10
    currentBit = 1
    # 统计一下最大值的bitCount（有多少位），因为比较多少次，是有最大值的位数决定的
    while currentBit <= 10 ** (bitCount - 1):  # 开始循环的进行每一个位的比较
        res = []
        buckets = [[] for _ in range(10)]  # 桶排序
        for i in arr:
            currentBitNum = get_bite(i, currentBit)
            buckets[currentBitNum].append(i)
        for i in range(10):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
        arr = res
        currentBit *= 10
    return arr


def main():
    list = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为：", list)
    print("排序后序列为：", cardinality_sort(list))


if __name__ == '__main__':
    main()
