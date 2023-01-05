# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 移动零.py
@time: 2023/1/5 21:52
"""
from typing import List

# 题目链接：https://leetcode.cn/problems/move-zeroes/?favorite=2cktkvj
"""
思路及解法

使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。
注意到以下性质：
左指针左边均为非零数；
右指针左边直到左指针处均为零。
因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
