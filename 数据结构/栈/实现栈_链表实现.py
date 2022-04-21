# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 实现栈_链表实现.py
@time: 2022/4/20 22:12
"""

"""
程序功能：模拟栈的实现(链表实现)
"""


class LNode:
    def __init__(self, data=0, next=None):  # 节点数据统一以整数作为示例
        self.data = data
        self.next = next


class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    # 判断stack是否为空,如果为空返回true，否则返回false
    def empty(self):
        if self.next is None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.next
        while p is not None:
            p = p.next
            size += 1
        return size

    # 入栈：把e放到栈顶
    def push(self, e):
        p = LNode

        p.data = e
        p.next = self.next
        self.next = p

    # 出栈，同时返回栈顶元素
    def pop(self):
        tmp = self.next
        if tmp is not None:
            self.next = tmp.next
            return tmp.data
        print("栈已经为空")
        return None

    # 取得栈顶元素
    def top(self):
        if self.next is not None:
            return self.next.data
        print("栈已经为空")
        return None


def main():
    stack = MyStack()
    stack.push(1)
    print("栈顶元素为：" + str(stack.top()))
    print("栈大小为：" + str(stack.size()))
    stack.pop()
    print("弹栈成功")
    stack.pop()


if __name__ == "__main__":
    main()
