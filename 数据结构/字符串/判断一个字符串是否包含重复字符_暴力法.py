# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个字符串是否包含重复字符_暴力法.py
@time: 2022/5/20 23:12
"""
"""

程序功能：判断字符串中是否有相同的字符
"""


def isDup(strs):
    lens = len(strs)
    i = 0
    while i < lens:  # 双重循环遍历（时间复杂度为O(N^2)）
        j = i + 1
        while j < lens:
            if list(strs)[j] == list(strs)[i]:
                return True
            j += 1
        i += 1
    return False


def main():
    strs = "GOOD"
    result = isDup(strs)
    if result:
        print(strs + "中有重复字符")
    else:
        print(strs + "中没有重复字符")


if __name__ == "__main__":
    main()
