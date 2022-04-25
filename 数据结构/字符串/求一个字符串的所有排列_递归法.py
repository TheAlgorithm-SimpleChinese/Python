# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求一个字符串的所有排列_递归法.py
@time: 2022/4/25 21:59
"""


# 交换字符数组下标为i和j对应的字符
def swap(str, i, j):
    tmp = str[i]
    str[i] = str[j]
    str[j] = tmp


"""
方法功能：对字符串中的字符进行全排列
输入参数：str为待排序的字符串，start为待排序的子字符串的首字符下标
"""


def Permutation(str, start):
    if str is None or start < 0:  # 字符串为空或者首字符下标小于零
        return
    # 完成全排列后输出当前排列的字符串
    if start == len(str) - 1:
        print(''.join(str))
    else:
        i = start
        while i < len(str):
            # 交换start与i所在位置的字符
            swap(str, start, i)
            # 固定第一个字符，对剩余的字符进行全排列
            Permutation(str, start + 1)
            # 还原start与i所在位置的字符
            swap(str, start, i)
            i += 1


def Permutation_transe(s):
    str = list(s)
    Permutation(str, 0)


def main():
    s = "abc"
    Permutation_transe(s)


if __name__ == "__main__":  # 书中两个等号之间有空白
    main()

