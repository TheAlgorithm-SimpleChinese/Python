# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 链表的逆序_递归法.py
@time: 2022/4/17 10:56
"""

"""
程序功能：实现链表的逆序
"""


class Node:
    """创建节点类"""

    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


"""
方法功能：对不带头结点的单链表进行逆序
输入参数：head:链表头结点
"""


def RecursiveReverse(head):
    # 如果链表为空或者链表中只有一个元素
    if head is None or head.next is None:
        return head
    else:
        # 反转后面的结点
        new_head = RecursiveReverse(head.next)
        # 把当前遍历的结点加到后面结点逆序后链表的尾部
        head.next.next = head
        head.next = None
    return new_head


"""
方法功能：对带头结点的单链表进行逆序
输入参数：head:链表头结点
"""


def Reverse(head):
    if head is None:
        return
        # 获取链表第一个结点
    firstNode = head.next
    # 对链表进行逆序
    new_head = RecursiveReverse(firstNode)
    # 头结点指向逆序后链表的第一个结点
    head.next = new_head
    return new_head


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
