# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 盛最多水的容器_双指针.py
@time: 2022/9/7 10:23
"""

"""
时间复杂度：O(N)，双指针总计最多遍历整个数组一次。
空间复杂度：O(1)，只需要额外的常数级别的空间。
"""


# 题目链接：https://leetcode.cn/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


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
