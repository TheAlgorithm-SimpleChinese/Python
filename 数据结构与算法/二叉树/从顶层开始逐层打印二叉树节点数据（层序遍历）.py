# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 从顶层开始逐层打印二叉树节点数据（层序遍历）.py
@time: 2022/6/5 19:33
"""
"""
程序功能：从顶层开始逐层打印二叉树节点数据（层序遍历）
"""

from collections import deque


class BiTNode:
    """
    二叉树的结构，每一个节点都拥有左孩子和右孩子指针
    """

    def __init__(self, data=0, lchild=None, rchild=None) -> None:  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


# 方法功能：把有序数组转换为二叉树
def array_to_tree(arr, start, end):
    if end >= start:
        root = BiTNode()
        mid = (start + end + 1) // 2
        # 树的根结点为数组中间的元素
        root.data = arr[mid]
        # 递归的用左半部分数组构造root的左子树
        root.lchild = array_to_tree(arr, start, mid - 1)
        # 递归的用右半部分数组构造root的右子树
        root.rchild = array_to_tree(arr, mid + 1, end)

    else:
        root = None
    return root


"""
方法功能：用层序遍历的方式打印出二叉树结点的内容
输入参数：root:二叉树根结点
"""


def printTreeLayer(root):
    if root is None:
        return
    queue = deque()
    # 树根结点进队列
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        # 访问当前结点
        print(p.data, end=" ")
        # 如果这个结点的左孩子不为空则入队列
        if p.lchild is not None:
            queue.append(p.lchild)
        # 如果这个结点的右孩子不为空则入队列
        if p.rchild is not None:
            queue.append(p.rchild)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("数组：", end="")
    i = 0
    while i < len(arr):
        print(arr[i], end=" ")
        i += 1
    print('\n')
    root = array_to_tree(arr, 0, len(arr) - 1)
    print("树的层序遍历结果为:", end="")
    printTreeLayer(root)


if __name__ == "__main__":
    main()
