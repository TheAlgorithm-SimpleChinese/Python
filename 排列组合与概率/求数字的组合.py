# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 求数字的组合.py
@time: 2022/6/13 13:30
"""
"""
需求描述:用1、2、2、3、4、5这六个数字，写一个main函数，打印出所有不同的排列，
例如:512234、412325,要求：“4”不能在第三位，“3”与“5”不能相连。
"""


class Test:
    def __init__(self, numbers):
        # self.numbers=[1, 2, 2, 3, 4, 5]
        self.numbers = numbers
        # 用来标记图中结点是否被遍历过
        self.visited = [None] * len(self.numbers)
        # 图的二维数组表示
        self.graph = [([None] * len(self.numbers)) for _ in range(len(self.numbers))]
        self.n = 6
        # 用来标记图中结点是否被遍历过
        # self.visited=None
        # 图的二维数组表示
        # self.graph=None
        # 数字的组合
        self.combination = ''
        # 存放所有的组合
        self.s = set()

    """
    **方法功能：对图从结点start位置开始进行深度遍历
    ** 输入参数：start：遍历的起始位置
    """

    def depthFirstSearch(self, start):
        self.visited[start] = True
        self.combination += str(self.numbers[start])
        if len(self.combination) == self.n:
            # 4不出现在第三个位置
            if self.combination.index("4") != 2:
                self.s.add(self.combination)
        j = 0
        while j < self.n:
            if self.graph[start][j] == 1 and self.visited[j] is False:
                self.depthFirstSearch(j)
            j += 1
        self.combination = self.combination[:-1]
        self.visited[start] = False

    # 方法功能：获取1、2、2、3、4、5的左右组合，使得"4"不能在第三位，"3"与"5"不能相连
    def getAllCombinations(self):
        # 构造图
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if i == j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j] = 1
                j += 1
            i += 1
            # 确保在遍历的时候3与5是不可达的
        self.graph[3][5] = 0
        self.graph[5][3] = 0
        # 分别从不同的结点出发深度遍历图
        i = 0
        while i < self.n:
            self.depthFirstSearch(i)
            i += 1

    def printAllCombinations(self):
        for strs in self.s:
            print(strs)


def main():
    arr = [1, 2, 2, 3, 4, 5]
    t = Test(arr)
    t.getAllCombinations()
    # 打印所有组合
    t.printAllCombinations()


if __name__ == "__main__":
    main()
