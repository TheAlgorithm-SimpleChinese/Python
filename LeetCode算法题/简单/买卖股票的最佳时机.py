# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 买卖股票的最佳时机.py
@time: 2022/12/15 20:22
"""
from typing import List

# 题目链接:https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?favorite=2cktkvj
"""
解题思路：遍历数组，选取当前价格与前序价格相差最大的进行交易
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        pre = prices[0]
        for price in prices[1:]:
            if price - pre > ans:
                ans = price - pre
            if price < pre:
                pre = price
        return ans


if __name__ == '__main__':
    solve1 = Solution()
    print(solve1.maxProfit([7, 1, 5, 3, 6, 4]))
