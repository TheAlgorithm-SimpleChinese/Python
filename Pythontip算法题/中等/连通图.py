# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 连通图.py
@time: 2022/12/5 21:19
"""
import math

'''
1) n个节点的无向图的形态有S(n) = 2^C(n,2)种，假设其中连通图的种类有L(n)种，非连通图的种类有F(n)种，则L(n) = S(n) - F(n)
2) 求F(n)，对于任意一个节点A来说，A的连通形态可能为与1到(n-1)个
   a. 为1时，其他(n-1)个节点为任意形态，则此时非连通图的种类为S(n-1);
   b. 为2时，任选一个节点与A连通，其他n-2个节点为任意形态，此时非连通图的种类为C(n-1, 1)*L(2)*S(n-2)
   c. 为k时，1<=k<=n-1，此时非连通图的种类为C(n-1, k-1)*L(k)*S(n-k)
   d. 以上相加，即为F(n)
'''

n = 3


# 组合函数计算，从n个里面取k个，有多少种取法，用公式计算
def C(n, k):
    m = min(k, n - k)
    f = 1
    for i in range(m):
        f *= n
        n -= 1
    return f // math.factorial(m)


# 定义S(n)为n个节点的无向图的形态总数，L(n)为n个节点连通图的总数，依次求L[i]
S = [0, 1] + [2 ** C(_, 2) for _ in range(2, n + 1)]
L = [0, 1]
for i in range(2, n + 1):
    f_i = 0
    for k in range(1, i):
        f_i += C(i - 1, k - 1) * L[k] * S[i - k]
    l_i = S[i] - f_i
    L.append(l_i)
print(L[-1])
