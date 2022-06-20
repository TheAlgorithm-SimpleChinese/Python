# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个字符串是否由另外一个字符串旋转得到.py
@time: 2022/6/20 15:54
"""


# 函数功能：判断str2是否为str1的子串
def isSubstring(str1, str2):
    return str1.find(str2) != -1


# 函数功能：判断str2是否可以通过旋转str1得到
def rotateSame(str1, str2):
    if str1 is None or str2 is None:
        return False
    len1 = len(str1)
    len2 = len(str2)
    # 判断两个字符串长度是否相等，如果不相等，那么不可能通过旋转得到
    if len1 != len2:
        return False
    # 申请临时空间存储str1str1，多申请了一个空间存储‘\0’
    tmp = [None] * (2 * len1 + 1)
    # 是tmp为str1str1
    i = 0
    while i < len1:
        tmp[i] = list(str1)[i]
        tmp[i + len1] = list(str1)[i]
        i += 1
    tmp[2 * len1] = '\0'
    # 判断str2是否为tmp的子串
    result = isSubstring(''.join(tmp), str2)
    return result


def main():
    str1 = "waterbottle"
    str2 = "erbottlewat"
    result = rotateSame(str1, str2)
    if result:
        print(str2 + "可以通过旋转" + str1 + "得到")
    else:
        print(str2 + "不可以通过旋转" + str1 + "得到")


if __name__ == "__main__":
    main()
