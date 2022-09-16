# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 寻找两个正序数组的中位数_归并排序.py
@time: 2022/9/15 8:12
"""


# 题目链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = list()
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        # 合并两个有序列表
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
            if i == m and j != n:
                nums3 += (nums2[j:n])
            if j == n and i != m:
                nums3 += (nums1[i:m])
        if len(nums3) % 2 != 0:
            res = nums3[len(nums3) // 2]  # 列表长度为奇数
        else:
            res = (nums3[((m + n) // 2) - 1] + nums3[(m + n) // 2]) / 2  # 列表长度为偶数
        return res


# 示例
if __name__ == '__main__':
    # 示例1
    nums1 = [1, 3]
    nums2 = [2]
    solve1 = Solution()
    print(solve1.findMedianSortedArrays(nums1, nums2))
    # 示例2
    nums1 = [1, 2]
    nums2 = [3, 4]
    solve2 = Solution()
    print(solve2.findMedianSortedArrays(nums1, nums2))
