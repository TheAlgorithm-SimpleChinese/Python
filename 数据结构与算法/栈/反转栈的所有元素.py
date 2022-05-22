# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 反转栈的所有元素.py
@time: 2022/5/17 22:10
"""


# Python中没有栈的模块，所以先新建一个栈类
class Stack:
    """
    模拟栈
    """

    def __init__(self):
        self.items = []

    # 判断栈是否为空
    def empty(self):
        return len(self.items) == 0

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    # 压栈
    def push(self, item):
        self.items.append(item)


"""
方法功能：把栈底元素移动到栈顶
参数：s 栈的引用
"""


def moveBottomToTop(s):
    if s.empty():
        return
    top1 = s.peek()
    s.pop()  # 弹出栈顶元素
    if not s.empty():
        # 递归处理不包含栈顶元素的子栈
        moveBottomToTop(s)
        top2 = s.peek()
        s.pop()
        # 交换栈顶元素与子栈栈顶元素
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)


def reverse_stack(s):
    if s.empty():
        return
        # 把栈底元素移动到栈顶
    moveBottomToTop(s)
    top = s.peek()
    s.pop()
    # 递归处理子栈
    reverse_stack(s)
    s.push(top)


def main():
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    reverse_stack(s)
    print("翻转后出栈顺序为:")
    while not s.empty():
        print(s.peek(), end=" ")
        s.pop()


if __name__ == "__main__":
    main()
