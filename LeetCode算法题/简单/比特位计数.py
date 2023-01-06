# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 比特位计数.py
@time: 2023/1/6 22:15
"""
from typing import List


# 题目链接：https://leetcode.cn/problems/counting-bits/?favorite=2cktkvj
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(bin(i).count("1"))
        return res
