# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 异或求和.py
@time: 2022/10/21 21:28
"""
N = 5


# 1.从0开始找规律，发现每4个数字结果为0，即（n+1） % 4 == 0时，结果为0
# 2.所以只需要算最后一个0，后面几位数字的异或结果即可
# 3.异或运算顺序不影响结果，所以可以从n往前算，遇到（n+1） % 4 == 0即结束
def solve_it(n):
    answer = 0
    for i in range(n, 0, -1):
        if (i + 1) % 4 == 0:
            break
        answer ^= i
    return answer


print(solve_it(N))
