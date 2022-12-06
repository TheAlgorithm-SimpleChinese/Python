# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 有效的括号.py
@time: 2022/12/6 21:08
"""
# 题目链接：https://leetcode.cn/problems/valid-parentheses/?favorite=2cktkvj
"""
解题思路：栈

"""


class Solution:

    def is_valid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


# 示例
if __name__ == '__main__':
    # 示例1
    s1 = "()"
    solve1 = Solution()
    print(solve1.is_valid(s1))
    # 示例2
    s2 = "()[]{}"
    solve2 = Solution()
    print(solve2.is_valid(s2))
    # 示例3
    s3 = "(]"
    solve3 = Solution()
    print(solve3.is_valid(s3))
