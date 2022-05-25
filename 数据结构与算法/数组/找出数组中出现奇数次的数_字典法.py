# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 找出数组中出现奇数次的数_字典法.py
@time: 2022/5/25 20:07
"""
"""
题目描述：数组中有N+2个数，其中，N个数出现偶数次，2个数出现奇数次，两个数不相等，请用O（1）的时间复杂度
找出这两个数。不需要位置，只需找出这两个数。
"""
"""
程序功能：找出数组中出现奇数次的数
"""


def get2Num(arr):
    if arr is None or len(arr) < 1:
        print("参数不合理")
        return
    dic = dict()
    i = 0
    while i < len(arr):
        # dic中没有这个数字，说明第一次出现，value赋值为1
        if arr[i] not in dic:
            dic[arr[i]] = 1
        # 当前遍历的值在dic中存在，说明前面出现过，value赋值为0
        else:
            dic[arr[i]] = 0
        i += 1
    for k, v in dic.items():  # 值为1则为奇数次的数
        if v == 1:
            print(int(k))


def main():
    arr = [3, 5, 6, 6, 5, 7, 2, 2]
    get2Num(arr)


if __name__ == "__main__":
    main()
