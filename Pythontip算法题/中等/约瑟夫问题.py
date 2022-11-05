# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 约瑟夫问题.py
@time: 2022/11/5 20:55
"""
n = 6
m = 2
ysf = []
for i in range(n):
    ysf.append(i + 1)
cnt = n
j = 0
while cnt != 1:
    i = 0
    while i < m:
        if j == n:
            j = 0
        else:
            if ysf[j] == 0:
                j = j + 1
            else:
                i = i + 1
                j = j + 1

    cnt = cnt - 1
    # print(ysf[j-1])
    ysf[j - 1] = 0
for i in ysf:
    if i != 0:
        print(i)
