# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 两数之和_哈希表法.py
@time: 2022/9/6 15:28
"""
# 题目链接：https://leetcode.cn/problems/two-sum/
"""
题目分析：
注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。
因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引。
使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N^2)降低到 O(1)。
这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。
复杂度分析:


"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
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
