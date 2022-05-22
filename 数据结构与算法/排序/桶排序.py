# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 桶排序.py
@time: 2022/4/29 22:50
"""
"""
算法功能：桶排序
"""


def bucket_sort(arr):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num - min_num) / len(arr)
    # 桶数组
    count_list = [[] for _ in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i - min_num) // bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)
    return arr


def main():
    list = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为：", list)
    print("排序后序列为：", bucket_sort(list))


if __name__ == '__main__':
    main()
