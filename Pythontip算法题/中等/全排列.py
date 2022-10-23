# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 全排列.py
@time: 2022/10/23 21:02
"""
s = "abcd"
L = set()


def all_sort(s1):
    lens = len(s1)
    if lens == 1:
        return {s1}
    if lens == 2:
        return {s1, s1[::-1]}

    for _ in s1:
        return {i + j for i in s1 for j in all_sort(s1.replace(i, '', 1))}


List = list(all_sort(s))
List.sort()
for each in List:
    print(each)
