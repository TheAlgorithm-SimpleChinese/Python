# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 设计一个排序系统.py
@time: 2022/5/28 22:41
"""
"""
程序功能：设计一个排序系统
"""
from collections import deque


class User:
    def __init__(self, ID, name):
        self.ID = ID  # 唯一标识一个用户
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSeq(self):
        return self.seq

    def setSeq(self, seq):
        self.seq = seq

    def getId(self):
        return self.ID

    def equals(self, arg0):
        o = arg0
        return self.ID == o.getId()

    def toString(self):
        return "ID:" + str(self.ID) + " name:" + self.name + " seq:" + str(self.seq)


class MyQueue:
    def __init__(self):
        self.q = deque()

    def enQueue(self, u):  # 进入队列尾部
        u.setSeq(len(self.q) + 1)
        self.q.append(u)

    # 队头出队列
    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    # 队列中的人随机离开
    def deQueuemove(self, u):
        self.q.remove(u)
        self.updateSeq()

    # 出队列后更新队列中每个人的序列
    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    # 打印队列的信息
    def printList(self):
        for u in self.q:
            print(u.toString())


def main():
    u1 = User(1, "user1")
    u2 = User(2, "user2")
    u3 = User(3, "user3")
    u4 = User(4, "user4")

    queue = MyQueue()

    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)

    queue.printList()
    print("=====================")
    queue.deQueue()  # 队首元素u1出队列
    queue.deQueuemove(u3)  # 队列中间的元素u3出队列
    queue.printList()


if __name__ == "__main__":
    main()
