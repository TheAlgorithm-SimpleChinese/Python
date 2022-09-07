# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 盛最多水的容器_暴力法.py
@time: 2022/9/7 9:46
"""


# 题目链接：https://leetcode.cn/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        length = len(height)
        max = 0
        for i in range(length - 1):
            if height[i] > max / (length - i - 1):
                for j in range(i + 1, length):
                    water = (j - i) * min(height[i], height[j])
                    if max < water:
                        max = water
        return max


# 示例
if __name__ == '__main__':
    # 示例1
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solve1 = Solution()
    print(solve1.maxArea(height))
    # 示例2
    height = [1, 1]
    solve2 = Solution()
    print(solve2.maxArea(height))
