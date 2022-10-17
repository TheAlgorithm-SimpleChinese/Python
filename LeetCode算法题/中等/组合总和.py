# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 组合总和.py
@time: 2022/10/17 22:02
"""
def combination_sum(arr: list, target: int):
    res = []  # 保存结果
    arr.sort()
    cur = []  # 表示当前数字

    def back(start):
        if sum(cur) > target:
            return
        if sum(cur) == target:
            res.append(cur[:])
            return
        for i in range(start, len(arr)):
            if sum(cur) + arr[i] > target:
                break
            cur.append(arr[i])
            back(i)
            cur.pop()

    back(0)
    return res


if __name__ == '__main__':
    array = [2, 3, 6, 7]
    print(combination_sum(array, 7))
