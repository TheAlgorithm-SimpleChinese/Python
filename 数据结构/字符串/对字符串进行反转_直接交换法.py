# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 对字符串进行反转_直接交换法.py
@time: 2022/5/11 21:05
"""
"""
算法功能：对字符串进行反转
"""


def reverseStr(strs):
    ch = list(strs)
    lens = len(ch)
    i = 0
    j = lens - 1
    while i < j:
        # Python中不能直接对字符串进行异或操作，所以借助ord和chr函数。
        ch[i] = chr(ord(ch[i]) ^ ord(ch[j]))
        ch[j] = chr(ord(ch[i]) ^ ord(ch[j]))
        ch[i] = chr(ord(ch[i]) ^ ord(ch[j]))
        i += 1
        j -= 1
    return ''.join(ch)


def main():
    str = "abcdefg"
    print("字符串" + str + "翻转后为：")
    print(reverseStr(str))


if __name__ == '__main__':
    main()
