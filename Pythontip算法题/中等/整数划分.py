# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 整数划分.py
@time: 2022/10/26 14:15
"""
"""
思路：

假设f(n, m)
表示将n划分为最大加数不超过整数m的方法数.

f（n, m） =:四种情况

1
n = 1 or m = 1

f(n, n)
n < m

1 + f(n, n - 1)
n = m

f(n, m - 1) + f(n - m, m)
n > m > 1

"""


# 所以递归即可：

def solve_it(n, m):
    if n == 1 or m == 1:
        return 1
    elif n == m:
        return 1 + solve_it(n, m - 1)
    elif n < m:
        return solve_it(n, n)
    else:
        return solve_it(n, m - 1) + solve_it(n - m, m)


N = 4
print(solve_it(N, N))

# 但由于可能子问题可能重复计算，时间复杂度过高，所以可以考虑自底向上把算过的数据存在一个二维列表里。
