# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 多数元素.py
@time: 2023/1/4 20:35
"""
# 题目链接：https://leetcode.cn/problems/majority-element/?favorite=2cktkvj
"""
摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」，
算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。

算法可以分为两个阶段：

对抗阶段：分属两个候选人的票数进行两两对抗抵消
计数阶段：计算对抗结果中最后留下的候选人票数是否有效

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0

        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major
