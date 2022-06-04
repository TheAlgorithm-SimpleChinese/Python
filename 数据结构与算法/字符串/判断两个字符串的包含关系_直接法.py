# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 判断两个字符串的包含关系.py
@time: 2022/6/4 22:48
"""
"""
方法功能：判断两个字符串是否为包含关系
输入参数：s1与s2为两个字符串
"""


def isContain(str_1, str_2):
    len1 = len(str_1)
    len2 = len(str_2)
    # 字符串ch1比ch2短
    if len1 < len2:
        i = 0
        while i < len1:
            j = 0
            while j < len2:
                if list(str_1)[i] == list(str_2)[j]:
                    break
                j += 1
            if j >= len2:
                return False
            i += 1
    else:
        # 字符串ch1比ch2长
        i = 0
        while i < len2:
            j = 0
            while j < len1:
                if list(str_1)[j] == list(str_2)[i]:
                    break
                j += 1
            if j >= len1:
                return False
            i += 1
    return True


def main():
    str1 = "abcdef"
    str2 = "acf"
    is_Contain = isContain(str1, str2)
    print(str1 + "与" + str2)
    if is_Contain:
        print("有包含关系")
    else:
        print("没有包含关系")


if __name__ == "__main__":
    main()
