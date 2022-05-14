# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 实现字符串的匹配_直接计算法.py
@time: 2022/5/8 23:30
"""
"""
方法功能：判断p是否为s的子串，如果是，那么返回p在s中第一次出现的下标，否则返回-1
输入参数：s和p分别为主串和模式串
"""


def match(s, p):
    # 检查参数的合理性
    if s is None or p is None:
        print("参数不合理")
        return -1
    slen = len(s)  # 字符串s的长度
    plen = len(p)  # 字符串p的长度
    # p肯定不是s的子串
    if slen < plen:
        return -1
    i = 0
    j = 0
    while i < slen and j < plen:
        if list(s)[i] == list(p)[j]:
            # 如果相同，那么继续比较后面的字符
            i += 1
            j += 1
        else:
            # 后退回去重新比较
            i = i - j + 1  # 后退回到下一个字符开始比较
            j = 0
            if i > slen - plen:  # 剩余字符串长度小于p长度
                return -1
    if j >= plen:  # 匹配成功
        return i - plen
    return -1


def main():
    s = "xyzabcd"
    p = "abc"
    print("p在s中第一次出现的下标为", match(s, p))


if __name__ == "__main__":
    main()
