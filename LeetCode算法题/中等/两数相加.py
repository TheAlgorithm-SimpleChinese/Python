# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 两数相加.py
@time: 2022/9/13 11:07
"""

# 题目链接：https://leetcode.cn/problems/add-two-numbers/?favorite=2cktkvj
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化列表
        head = tree = ListNode()

        val = tmp = 0
        # 当三者有一个不为空时继续循环
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            # tmp表示进位
            tmp = val // 10
            # val表示保留位
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next


# 示例
if __name__ == '__main__':
    # 示例1
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solve1 = Solution()
