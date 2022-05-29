# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 实现LRU缓存方案.py
@time: 2022/5/29 21:49
"""
"""
程序功能：实现LRU缓存方案
"""

from collections import deque


class LRU:
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize  # 缓存大小
        self.queue = deque()
        self.hashSet = set()

    # 判断缓存队列是否已满
    def isQueueFull(self):
        return len(self.queue) == self.cacheSize

    # 把页号为pageNum的页缓存到队列中，同时也添加到Hash表中
    def enqueue(self, pageNum):
        # 如果队列满了，需要删除队尾的缓存的页
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        # 把新缓存的结点同时添加到hash表中
        self.hashSet.add(pageNum)

    """
    当访问某一个page的时候会调用这个函数，对于访问的page有两种情况：
    1. 如果page在缓存队列中，直接把这个结点移动到队首
    2. 如果page不在缓存队列中，把这个page缓存到队首。
    """
    def accessPage(self, pageNum):
        # page不在缓存队列中，把它缓存到队首
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        # page已经在缓存队列中了，移动到队首
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    # 输入U缓存的队列
    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


def main():
    # 假设缓存大小为3
    lru = LRU(3)
    # 访问page
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    # 通过上面的访问序列后，缓存的信息为
    lru.printQueue()


if __name__ == "__main__":
    main()
