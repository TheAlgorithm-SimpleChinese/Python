# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 字符串编辑.py
@time: 2022/11/28 23:44
"""
a = "pale"
b = "ple"


# 插入和删除可以用一个函数表示，该函数默认len(a) < len(b)
def Insert_Del(a, b):
    for each in b:
        if each not in a:
            break
    index = b.find(each)
    if b[:index] + b[index + 1:] == a:
        return 1
    else:
        return 0


# 去掉需要替换的第一个字符看剩余的是否相等
def Repalce(a, b):
    for each in b:
        if each not in a:
            break
    index = b.find(each)
    if b[:index] + b[index + 1:] == a[:index] + a[index + 1:]:
        return 1
    else:
        return 0


if len(a) == len(b) and Repalce(a, b):
    print('YES')
elif (len(a) - len(b) == 1) and Insert_Del(b, a):
    print('YES')
elif (len(a) - len(b) == -1) and Insert_Del(a, b):
    print('YES')
else:
    print('NO')
