# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 移除无序链表中的重复项_递归法.py
@time: 2022/4/17 21:40
"""

"""
** 方法功能：对带头结点的无序单链表删除重复的结点 
** 输入参数：head:链表头结点
"""


class Node:
    """创建节点类"""

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def removeDupRecursion(head):
    if head.next is None:
        return head
    cur = head
    # 对以head.next为首的子链表删除重复的结点
    head.next = removeDupRecursion(head.next)
    pointer = head.next
    # 找出以head.next为首的子链表中与head结点相同的结点并删除
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head


"""
方法功能：对带头结点的单链删除重复结点 输入参数：head:链表头结点
"""


def removeDup(head):
    if head is None:
        return
    head.next = removeDupRecursion(head.next)


def main():
    i = 1
    head = Node()  # 创建头结点
    head.next = None
    cur = head
    while i < 7:  # 初始化链表
        tmp = Node()
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("删除重复结点前：", end=" ")
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    removeDup(head)
    print("\n删除重复结点后：", end=" ")
    cur = head.next
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next


if __name__ == "__main__":
    main()
