# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 将链表向右旋转K个位置.py
@time: 2022/4/19 21:02
"""


# 引申：如何将单链表向右旋转k个位置
class LNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    # 方法功能：把链表右旋k个位置


def RotateK(head, k):
    if head is None or head.next is None:
        return
    # fast指针先走k步，然后与slow指针同时向后走
    slow, fast = head.next, head.next
    i = 0
    while i < k and fast is not None:  # 前移k步
        fast = fast.next
        i += 1
        # 判断k是否已超出链表长度
    if i < k:
        return
        # 循环结束后slow指向链表倒数第k+1个元素，fast指向链表最后一个元素
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    tmp = slow
    slow = slow.next
    tmp.next = None
    fast.next = head.next
    head.next = slow


def ConstructList():
    i = 1
    head = LNode()
    head.next = None
    cur = head
    # 构造第一个链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    return head


# 顺序打印单链表结点的数据
def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next


def main():
    head = ConstructList()
    print("旋转前：")
    PrintList(head)
    RotateK(head, 3)
    print("\n旋转后: ")
    PrintList(head)


if __name__ == "__main__":
    main()
