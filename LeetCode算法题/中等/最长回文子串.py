# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 最长回文子串.py
@time: 2022/9/20 16:02
"""


# 题目链接：https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        # dp[i][j]表示是s[i..j]是否回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


# 示例
if __name__ == '__main__':
    # 示例1
    s = "babad"
    solve1 = Solution()
    print(solve1.longestPalindrome(s))
    # 示例2
    s = "cbbd"
    solve2 = Solution()
    print(solve2.longestPalindrome(s))
