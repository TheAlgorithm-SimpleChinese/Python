# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 相交链表.py
@time: 2023/1/3 21:25
"""
# 题目链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/?favorite=2cktkvj
"""
一种比较巧妙的方式是，分别为链表A和链表B设置指针A和指针B，然后开始遍历链表，如果遍历完当前链表，则将指针指向另外一个链表的头部继续遍历，直至两个指针相遇。
最终两个指针分别走过的路径为：
指针A :a+c+b
指针B :b+c+a
明显 a+c+b = b+c+a,因而如果两个链表相交，则指针A和指针B必定在相交结点相遇。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
