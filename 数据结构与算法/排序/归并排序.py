# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 归并排序.py
@time: 2022/4/27 21:11
"""
"""
算法功能：归并排序(升序、二路归并)
"""


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):  # 对左右两部分进行归并操作
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # 当左右部分还有剩余元素时间，添加到结果中
    result += right[j:]
    return result


def merge_sort(sortedlist):
    # 归并排序
    if len(sortedlist) <= 1:  # 如果列表为空或者只有一个数
        return sortedlist
    num = int(len(sortedlist) / 2)  # 把列表分为两部分
    # 对左右部分进行递归排序
    left = merge_sort(sortedlist[:num])
    right = merge_sort(sortedlist[num:])
    return merge(left, right)


def main():
    lists = [3, 4, 2, 8, 9, 5, 1]  # 测试列表
    print('排序前序列为:', lists)
    print('排序后结果为:', merge_sort(lists))


if __name__ == "__main__":
    main()
