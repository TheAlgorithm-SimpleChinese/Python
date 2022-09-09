# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 三数之和_排序_双指针.py
@time: 2022/9/9 10:33
"""
# 题目链接：https://leetcode.cn/problems/3sum/
"""
复杂度分析：
时间复杂度：O(N^2),其中N是数组nums的长度。
空间复杂度：O(logN)。我们忽略存储答案的空间，额外的排序的空间复杂度为 O(logN)。
然而我们修改了输入的数组nums，在实际情况下不一定允许，因此也可以看成使用了一个额外的组存储了nums的副本并进行排序，空间复杂度为 O(N)。
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        # 枚举a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的初始指针指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # 需要和上次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证b的指针在c的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# 示例
if __name__ == '__main__':
    # 示例1
    nums = [-1, 0, 1, 2, -1, -4]
    solve1 = Solution()
    print(solve1.threeSum(nums))
    # 示例2
    nums = [0, 1, 1]
    solve2 = Solution()
    print(solve2.threeSum(nums))
    # 示例3
    nums = [0, 0, 0]
    solve3 = Solution()
    print(solve3.threeSum(nums))
