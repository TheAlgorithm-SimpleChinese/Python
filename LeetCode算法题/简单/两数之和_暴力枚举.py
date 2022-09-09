# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 两数之和_暴力枚举.py
@time: 2022/9/6 14:59
"""

# 题目链接：https://leetcode.cn/problems/two-sum/
"""
题目分析：
最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，
因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。

复杂度分析:

时间复杂度：O(N^2)，其中N是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
空间复杂度：O(1)。
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 示例
if __name__ == '__main__':
    # 示例1
    nums = [2, 7, 11, 15]
    target = 9
    solve1 = Solution()
    print(solve1.twoSum(nums, target))
    # 示例2
    nums = [3, 2, 4]
    target = 6
    solve2 = Solution()
    print(solve2.twoSum(nums, target))
    # 示例3
    nums = [3, 3]
    target = 6
    solve3 = Solution()
    print(solve3.twoSum(nums, target))
