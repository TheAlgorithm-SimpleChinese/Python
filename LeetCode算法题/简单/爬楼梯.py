# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 爬楼梯.py
@time: 2022/12/10 21:39
"""
# 题目链接：https://leetcode.cn/problems/climbing-stairs/
"""
解题思路
n>2时，第n层为（n-1）与（n-2)层之和
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        s = [0 for i in range(n)]
        s[0] = 1
        s[1] = 2
        for i in range(2, n):
            s[i] = s[i - 1] + s[i - 2]
        return s[n - 1]

# 示例
if __name__ == '__main__':
    # 示例
    solve1 = Solution()
    print(solve1.climbStairs(2))
    # 示例2
    solve2 = Solution()
    print(solve2.climbStairs(3))