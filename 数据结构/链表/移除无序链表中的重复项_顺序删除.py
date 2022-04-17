# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 移除无序链表中的重复项_顺序删除.py
@time: 2022/4/17 17:31
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


def removeDup(head):
    if head is None or head.next is None:
        return
    outerCur = head.next  # 用于外层循环，指向链表第一个结点
    innerCur = None  # 用于内层循环用来遍历outerCur后面的结点
    innerPre = None  # innerCur的前驱结点
    while outerCur is not None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur is not None:
            # 找到重复的结点并删除
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        outerCur = outerCur.next


def main():
    i = 1
    head = Node()  # 创建头结点
    head.next = None
    tmp = None
    cur = head
    while i < 7:    # 初始化链表
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
