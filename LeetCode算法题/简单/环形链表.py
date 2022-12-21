# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 环形链表.py
@time: 2022/12/21 19:53
"""
# 题目链接:https://leetcode.cn/problems/linked-list-cycle/?favorite=2cktkvj
"""
解题思路：使用hash表记录已经访问过的节点
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 1. python map
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False
