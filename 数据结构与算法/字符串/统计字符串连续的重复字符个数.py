# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 统计字符串连续的重复字符个数.py
@time: 2022/5/31 22:07
"""
"""
程序功能：统计字符串中最长连续的重复字符个数
"""


def getMaxDupChar(s, startIndex, curMaxLen, maxLen):
    # 字符串遍历结束，返回最长连续重复字符串的长度
    if startIndex == len(s) - 1:
        return max(curMaxLen, maxLen)
    # 如果两个连续的字符相等，那么在递归调用的时候把当前最长串的长度加1
    if list(s)[startIndex] == list(s)[startIndex + 1]:
        return getMaxDupChar(s, startIndex + 1, curMaxLen + 1, maxLen)
        # 两个连续的子串不相等，求出最长串max(curMaxLen, maxLen),
    # 当前连续重复字符串的长度变为1
    else:
        return getMaxDupChar(s, startIndex + 1, 1, max(curMaxLen, maxLen))


def main():
    print("abbc的最长连续重复子串长度为：" + str(getMaxDupChar("abbc", 0, 1, 1)))
    print("aaabbcc的最长连续重复子串长度为：" + str(getMaxDupChar("aaabbcc", 0, 1, 1)))


if __name__ == "__main__":
    main()
