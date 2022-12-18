# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 反转链表.py
@time: 2022/12/18 22:01
"""
from typing import Optional

# 题目链接：https://leetcode.cn/problems/reverse-linked-list/?favorite=ex0k24j
"""
1.定义两个指针： pre 和 cur ；pre 在前 curcur 在后。
2.每次让 pre 的 next 指向 cur ，实现一次局部反转
3.局部反转完成之后，pre 和 cur 同时往前移动一个位置
4.循环上述过程，直至 pre 到达链表尾部
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
