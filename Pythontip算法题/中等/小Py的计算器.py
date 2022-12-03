# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 小Py的计算器.py
@time: 2022/12/3 22:00
"""
# 134. 小Py的计算器
S = 'abcdefghijklmnopqrstuvwxyz'


def N_add(s1, s2):
    l = max(len(s1), len(s2))
    s1 = s1.rjust(l, 'a')
    s2 = s2.rjust(l, 'a')
    R = ''
    jinwei = 0
    for i in range(l - 1, -1, -1):
        tmp = S.index(s1[i]) + S.index(s2[i]) + jinwei
        if tmp >= 26:
            tmp = tmp - 26
            jinwei = 1
        else:
            jinwei = 0
        R = S[tmp] + R
    if jinwei == 1:
        return 'b' + R
    else:
        return R


s1 = "dfe"
s2 = "feb"
print(N_add(s1, s2))
