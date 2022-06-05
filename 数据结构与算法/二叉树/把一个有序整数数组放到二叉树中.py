# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 把一个有序整数数组放到二叉树中.py
@time: 2022/6/5 19:17
"""
"""
程序功能：把一个有序整数数组放到二叉树中
"""


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


# 用中序遍历的方式打印出二叉树结点的内容
def printTreeMidOrder(root):
    if root is None:
        return
    # 遍历root结点的左子树
    if root.lchild is not None:
        printTreeMidOrder(root.lchild)
    # 遍历root结点
    print(root.data)
    # 遍历root结点的右子树
    if root.rchild is not None:
        printTreeMidOrder(root.rchild)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("数组：")
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1
    print('\n')
    root = array_to_tree(arr, 0, len(arr) - 1)
    print("转换成树的中序遍历为:")
    printTreeMidOrder(root)
    print('\n')


if __name__ == "__main__":
    main()
