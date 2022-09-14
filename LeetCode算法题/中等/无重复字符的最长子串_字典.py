# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 无重复字符的最长子串_字典.py
@time: 2022/9/14 15:29
"""


# 题目链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/?favorite=2cktkvj
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        # i是索引，c是字符
        for i, c in enumerate(s):
            # 字符出现在字典中且上次出现的下标大于当前长度的起始下标
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res


# 示例
if __name__ == '__main__':
    # 示例1
    s = "abcabcbb"
    solve1 = Solution()
    print(solve1.lengthOfLongestSubstring(s))
    # 示例2
    s = "bbbbb"
    solve2 = Solution()
    print(solve2.lengthOfLongestSubstring(s))
    # 示例3
    s = "pwwkew"
    solve3 = Solution()
    print(solve3.lengthOfLongestSubstring(s))
