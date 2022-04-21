# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 检测单链表是否有环且找出环入口.py
@time: 2022/4/19 21:24
"""


class LNode:
    def __init__(self, data=0, next=None):  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.next = next

    # 构造链表


def constructList():
    i = 1
    head = LNode()
    cur = head
    # 构造第一个链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = head.next.next.next
    return head


"""
方法功能：判断单链表是否有环
输入参数：head:链表头结点
返回值：None:无环，否则返回slow与fast相遇点的结点
"""


def isLoop(head):
    if head is None or head.next is None:
        return None
    # 初始slow与fast都指向链表第一个结点
    slow = head.next
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return None


"""
方法功能：找出环的入口点
输入参数：head:fast与slow相遇点
返回值：None:无环，否则返回slow与fast指针相遇点的结点
"""


def findLoopNode(head, meetNode):
    first = head.next
    second = meetNode
    while first != second:
        first = first.next
        second = second.next
    return first


def main():
    head = constructList()  # 头结点
    meetNode = isLoop(head)
    if meetNode is not None:
        print("有环")
        loopNode = findLoopNode(head, meetNode)
        print("环的入口点为：" + str(loopNode.data))
    else:
        print("无环")


if __name__ == "__main__":
    main()
