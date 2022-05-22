# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求两个字符串的最长公共子串_滑动比较法.py
@time: 2022/5/11 20:59
"""
"""
方法功能：获取两个字符串的最长公共字串 
输入参数：str1和str2为指向字符的指针
"""


def getMaxSubStr(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    maxLen = 0
    tmpMaxLen = 0
    maxLenEnd1 = 0
    sb = ''
    i = 0
    while i < len1 + len2:
        s1begin = s2begin = 0
        tmpMaxLen = 0
        if i < len1:
            s1begin = len1 - i
        else:
            s2begin = i - len1
        j = 0
        while (s1begin + j < len1) and (s2begin + j < len2):
            if list(s1)[s1begin + j] == list(s2)[s2begin + j]:
                tmpMaxLen += 1
            else:
                if (tmpMaxLen > maxLen):
                    maxLen = tmpMaxLen
                    maxLenEnd1 = s1begin + j
                else:
                    tmpMaxLen = 0
            j += 1
        if tmpMaxLen > maxLen:
            maxLen = tmpMaxLen
            maxLenEnd1 = s1begin + j
        i += 1
    i = maxLenEnd1 - maxLen
    while i < maxLenEnd1:
        sb = sb + list(s1)[i]
        i += 1
    return sb


if __name__ == "__main__":
    str1 = "abccade"
    str2 = "dgcadde"
    print("最长公共子串为：", getMaxSubStr(str1, str2))
