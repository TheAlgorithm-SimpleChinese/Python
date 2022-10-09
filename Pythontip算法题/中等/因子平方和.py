# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 因子平方和.py
@time: 2022/10/9 23:11
"""
# 利用平方和公式 1^2 + 2^2 + 3^2 + ... + N^2 = （N *（N+1）*（2N+1）） // 6

# F(N) 计算中 1^2 有N//1个， 2^2有N//2个，3^2有N//3个，..., N^2 有N//N个
N = 6

s = (N * (N + 1) * (2 * N + 1)) // 6
ls = (i * i * (N // i - 1) for i in range(1, N // 2 + 1))
s += sum(ls)
print(s)
