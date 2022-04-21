# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 找出单链表中的倒数第K个元素_快慢指针法.py
@time: 2022/4/19 20:49
"""
"""
方法一：顺序遍历链表两遍，求出链表长度，然后再求倒数第K个元素（代码略）
"""
"""
方法二：快慢指针法，设置两个指针，一个先行移动K步，然后再两个指针同时移动，
当第一个指针移动到链表尾时，第二个指针刚好是倒数第K个元素
"""


# 快慢指针法
class LNode:
    def __init__(self, data=0, next=None):  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.next = next

    # 构造一个单链表


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
        print(cur.data, end=" "),
        cur = cur.next


"""
方法功能：找出链表倒数第k个结点
输入参数：head:链表头结点
返回值：倒数第k个结点
"""


def FindLastK(head, k):
    if head is None or head.next is None:
        return head
    slow = head.next
    fast = head.next
    i = 0
    while i < k and fast is not None:
        fast = fast.next  # 前移k步
        i += 1
    if i < k:
        return None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


def main():
    head = ConstructList()  # 链表头指针
    print("链表：", end=" ")
    PrintList(head)
    result = FindLastK(head, 3)
    if result is not None:
        print("\n链表倒数第3个元素为：" + str(result.data))


if __name__ == "__main__":
    main()
