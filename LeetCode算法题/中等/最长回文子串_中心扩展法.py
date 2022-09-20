# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 最长回文子串_中心扩展法.py
@time: 2022/9/20 16:23
"""


# 题目链接：# 题目链接：https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


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
