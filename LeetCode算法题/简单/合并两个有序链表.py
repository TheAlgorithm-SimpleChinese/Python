# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 合并两个有序链表.py
@time: 2022/12/7 20:40
"""

# 题目链接：https://leetcode.cn/problems/merge-two-sorted-lists/?favorite=2cktkvj
"""
解题思路：
备注： 在 Python 中，and 和 or 都有提前截至运算的功能。

and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
例子：[] and 7 等于 []
代码流程：（按行数）

判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
对 l1 和 l2 重新赋值，使得 l1 指向比较小的那个节点对象
修改 l1 的 next 属性为递归函数返回值
返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.value > l2.value:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


# 示例
if __name__ == '__main__':
    # 示例1
    l1 = ListNode(1)  # 结点
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    solve1 = Solution()
    res = solve1.mergeTwoLists(l1, l2)
    while res.next is not None:
        print(res.value)
        res = res.next
        if res.next is None:
            print(res.value)
