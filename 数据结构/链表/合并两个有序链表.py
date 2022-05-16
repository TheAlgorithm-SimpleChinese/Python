# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 合并两个有序链表.py
@time: 2022/5/16 22:40
"""
"""

程序功能：合并两个有序链表
"""


class LNode:
    """创建节点类"""

    def __init__(self, data=0, next=None):  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.next = next


# 方法功能：构造链表
def ConstructList(start):
    i = start
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 2
    return head


def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next


"""
方法功能：合并两个升序排列的单链表
输入参数：head1与head2代表两个单链表

返回值：合并后链表的头结点
"""


def Merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next  # 用来遍历head1
    cur2 = head2.next  # 用来遍历head2
    head = None  # 合并后链表的头结点
    cur = None  # 合并后的链表在尾结点
    # 合并后链表的头结点为第一个结点元素最小的那个链表的头结点
    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next
    # 每次找链表剩余结点的最小值对应的结点连接到合并后链表的尾部
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    # 当遍历完一个链表后把另外一个链表剩余的结点链接到合并后的链表后面
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head


def main():
    head1 = ConstructList(1)
    head2 = ConstructList(2)
    print("链表1(head1): ")
    PrintList(head1)
    print("\n链表2(head2): ")
    PrintList(head2)
    print("\n合并后的链表：")
    head = Merge(head1, head2)
    PrintList(head)


if __name__ == "__main__":
    main()
