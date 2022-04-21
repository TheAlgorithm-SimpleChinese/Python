# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 链表的逆序_就地逆序.py
@time: 2022/4/17 10:35
"""

"""
程序功能：实现链表的逆序
"""


class Node:
    """创建节点类"""

    def __init__(self, data: int, next=None):  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.next = next


# 方法功能：对单链表进行逆序 输入参数：head:链表头结点
def Reverse(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    # pre = None  # 前驱结点
    # cur = None  # 当前结点
    # next = None  # 后继结点
    # 把链表首结点变为尾结点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历到的结点cur指向其前驱结点
    while cur.next is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 链表最后一个结点指向倒数第二个结点
    cur.next = pre
    # 链表的头结点指向原来链表的尾结点
    head.next = cur


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
