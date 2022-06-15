# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 拿到最多的金币.py
@time: 2022/6/15 14:13
"""
"""
10个房间里放着随机的金币。每个房间只能进入一次，并只能在一个房间中拿金币。
一个人采取如下策略：前4个房间只看不拿。随后的房间只要看到比前4个房间都多的金币
数，就拿。否则就拿最后一个房间的金币，编程计算这种策略那到最多金币的概率。
"""
import random

"""
方法功能：总共n个房间，判断用指定的策略是否能拿到最多金币
返回值：如果能拿到返回True，否则返回False
"""


def getMaxNum(n):
    if n < 1:
        print("参数不合法")
        return
    a = [None] * n
    # 随机生成n个房间里金币的个数
    i = 0
    while i < n:
        a[i] = random.uniform(1, n)  # 生成1～n的随机数
        i += 1
        # 找出前四个房间中最多的金币个数
    max4 = 0
    i = 0
    while i < 4:
        if a[i] > max4:
            max4 = a[i]
        i += 1
    i = 4
    while i < n - 1:
        if a[i] > max4:  # 能拿到最多的金币
            return True
        i += 1
    return False  # 不能拿到最多的金币


def main():
    monitorCount = 1000 + 0.0
    success = 0
    i = 0
    while i < monitorCount:
        if getMaxNum(10):
            success += 1
        i += 1
    print(success / monitorCount)


if __name__ == "__main__":
    main()
