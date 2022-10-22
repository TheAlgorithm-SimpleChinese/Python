# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 质数的数目.py
@time: 2022/10/22 22:30
"""
N = 10086


# (大于6)6倍以外的数分别有：6n+1，6n+2，6n+3，6n+4，6n+5
# 其中6n+2，6n+3，6n+4三个数都可以分解：
#   6n+2=2(3n+1)
#   6n+3=3(2n+1)
#   6n+4=2(3n+2)
# 所以以上三个数必不可能是素数，剩下的只有6n+1，6n+5可能存在素数
def solve_it(n):
    l = [0 for _ in range(n + 1)]
    l[:7] = [0, 0, 1, 1, 0, 1, 0]
    if n <= 6:
        return sum(l[:n + 1])
    else:
        # 这一步筛掉 2 和 3 的倍数
        for i in range(5, n - 1, 6):
            l[i] = l[i + 2] = 1
    j = 5
    while j <= int(n ** 0.5):
        if l[j] == 1:
            # 这一步筛掉 j*j,j*(j+2),j*(j+4)……
            for item in range(j * j, n + 1, 2 * j):
                l[item] = 0
        j += 2
    return sum(l)


print(solve_it(N))
