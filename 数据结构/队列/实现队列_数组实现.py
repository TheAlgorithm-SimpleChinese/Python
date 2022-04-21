# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 实现队列_数组实现.py
@time: 2022/4/17 21:59
"""

"""
程序功能：实现队列（数组实现）
"""


class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0  # 队列头
        self.rear = 0  # 队列尾

    # 判断队列是否为空
    def isEmpty(self):
        return self.front == self.rear

    # 返回队列的大小
    def size(self):
        return self.rear - self.front

    # 返回队列首元素
    def getFront(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]

    # 返回队列尾元素
    def getBack(self):
        if self.isEmpty():
            return None
        return self.arr[self.rear - 1]

    # 删除队列头元素
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列已经为空")

    # 把新元素加入队列尾
    def enQueue(self, item):
        self.arr.append(item)
        self.rear += 1


def main():
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print("队列头元素为：" + str(queue.getFront()))
    print("队列尾元素为：" + str(queue.getBack()))
    print("队列大小为：" + str(queue.size()))


if __name__ == "__main__":
    main()
