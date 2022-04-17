# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 链表的逆序_插入法.py
@time: 2022/4/17 10:57
"""


class Node:
    """创建节点类"""

    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


# 插入法
def Reverse(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    cur = None  # 当前结点
    next = None  # 后继结点
    cur = head.next.next
    # 设置链表第一个结点为尾结点
    head.next.next = None
    # 把遍历到结点插入到头结点的后面
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


# 递归
def ReversePrint(firstNode):
    if firstNode is None:
        return
    ReversePrint(firstNode.next)
    print(firstNode.data)


def main():

    head = Node(7, None)  # 创建头节点，存储节点个数
    cur = head
    for i in range(1, 8):  # 创建节点
        cur.next = Node(i, None)
        cur = cur.next
    print("逆序前:", end=' ')  # 输出逆序前节点值
    test = head.next
    while test is not None:
        print(test.data, end=' ')
        test = test.next
    print("\n逆序后:", end=' ')  # # 输出逆序前节点值
    Reverse(head)
    test = head.next
    while test is not None:
        print(test.data, end=' ')
        test = test.next


if __name__ == "__main__":
    main()
