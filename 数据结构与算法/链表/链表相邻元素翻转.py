# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 链表相邻元素翻转.py
@time: 2022/4/19 21:45
"""
"""
方法一：交换相邻结点的数据域
方法二：就地逆序，通过调整指针域的指向来直接调换相邻的两个结点
"""


class LNode:
    def __init__(self, data=0, next=None):  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.next = next


# 把链表相邻元素翻转
def reverse(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    cur = head.next  # 当前遍历结点
    pre = head  # 当前结点的前驱结点
    while cur is not None and cur.next is not None:
        next = cur.next.next  # next当前结点后继结点的后继结点
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next
        pre = cur
        cur = next


def main():
    i = 1
    head = LNode()
    head.next = None
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("顺序输出：", end="")
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    reverse(head)
    print("\n逆序输出：", end="")
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    cur = head.next
    while cur is not None:
        cur = cur.next


if __name__ == "__main__":
    main()
