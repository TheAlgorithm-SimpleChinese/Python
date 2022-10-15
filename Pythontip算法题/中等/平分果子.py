# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 平分果子.py
@time: 2022/10/15 11:02
"""
L = [1, 2, 3, 4, 5]
len_l = len(L)

sum_l = sum(L)

ans = 0

L.sort()
for i in range(2 ** len_l):
    # 依次排列组合
    b_i = str(bin(i))
    sum_d_l = sum_l
    d_L = [_ for _ in L]
    for index, value in enumerate(b_i[:1:-1]):
        # 如果当前二进制位是1，就去掉这个果子，丢掉。
        if value == '1':
            sum_d_l -= d_L[index]
            d_L[index] = 0

    # 为了减少下面的 遍历果子和背包的循环次数，将所有重量为0的果子都去掉了。
    d_L.sort(reverse=False)
    while d_L:
        if not d_L[-1]:
            d_L.pop()
        else:
            break

    if sum_d_l % 2 or not sum_d_l:
        continue

    if sum_d_l < ans * 2:
        continue

    target = sum_d_l // 2
    dp = [0] * (target + 1)
    dp[0] = 1

    # 遍历果子和背包。
    for n in d_L:
        i = target
        while i >= n:
            dp[i] = dp[i] + dp[i - n]
            i = i - 1
    if dp[target] > 0:
        ans = max(ans, target)

print(ans)
