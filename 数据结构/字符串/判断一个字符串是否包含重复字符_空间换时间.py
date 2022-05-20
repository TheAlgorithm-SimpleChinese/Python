# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断一个字符串是否包含重复字符_空间换时间.py
@time: 2022/5/20 23:14
"""
"""

程序功能：判断字符串中是否有相同的字符
"""


def isDup(strs):
    lens = len(strs)
    flags = [None] * 8  # 只需要8个32位的int，8*32=256位(假设常见字符只有256个)
    i = 0
    while i < 8:  # 把辅助空间全部置零
        flags[i] = 0
        i += 1
    i = 0
    while i < lens:
        index = ord(list(strs)[i]) // 32
        shift = ord(list(strs)[i]) % 32
        if (flags[index] & (1 << shift)) != 0:  # 每一位表示一个字符，把已有字符对应位置位1
            return True
        flags[index] |= (1 << shift)
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
