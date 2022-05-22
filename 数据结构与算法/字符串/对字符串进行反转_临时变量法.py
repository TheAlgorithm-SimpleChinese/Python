# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 对字符串进行反转_临时变量法.py
@time: 2022/5/8 23:29
"""
"""
算法功能：对字符串进行反转
"""


def reverseStr(str):
    ch = list(str)
    lens = len(ch)  # 获取字符串长度
    i = 0
    j = lens - 1
    while i < j:  # 移动交换直到首尾相遇
        tmp = ch[i]
        ch[i] = ch[j]
        ch[j] = tmp
        i += 1
        j -= 1
    return ''.join(ch)


def main():
    str = "abcdefg"
    print("字符串" + str + "翻转后为：")
    print(reverseStr(str))


if __name__ == '__main__':
    main()
