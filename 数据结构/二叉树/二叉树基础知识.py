# -*- coding: utf-8 -*-

"""
@author: liuyang
@software: PyCharm
@file: 二叉树基础知识.py
@time: 2022/4/21 18:57
"""


class BiTNode:
    """
    二叉树的结构，每一个节点都拥有左孩子和右孩子指针
    """

    def __init__(self, data=0, lchild=None, rchild=None) -> None:  # 节点数据统一以整数作为示例且初始值为0
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


# 遍历二叉树
def display(tree: BiTNode) -> None:  # 安顺序遍历二叉树

    if tree:
        display(tree.lchild)
        print(tree.data)
        display(tree.rchild)


# 二叉树深度
def depth_of_tree(tree: BiTNode) -> int:
    return 1 + max(depth_of_tree(tree.lchild), depth_of_tree(tree.rchild)) if tree else 0


# 判断是否是完全二叉树
def is_full_binary_tree(tree: BiTNode) -> bool:
    if not tree:
        return True
    if tree.lchild and tree.rchild:
        return is_full_binary_tree(tree.lchild) and is_full_binary_tree(tree.rchild)
    else:
        return not tree.lchild and not tree.rchild


def main() -> None:  # 测试主函数
    # 构建二叉树
    tree = BiTNode(1)
    tree.lchild = BiTNode(2)
    tree.rchild = BiTNode(3)
    tree.lchild.lchild = BiTNode(4)
    tree.lchild.rchild = BiTNode(5)
    tree.lchild.rchild.lchild = BiTNode(6)
    tree.rchild.lchild = BiTNode(7)
    tree.rchild.lchild.lchild = BiTNode(8)
    tree.rchild.lchild.lchild.rchild = BiTNode(9)

    print(is_full_binary_tree(tree))  # 判断是否是完全二叉树
    print(depth_of_tree(tree))  # 返回二叉树深度
    print("Tree is: ")
    display(tree)  # 遍历二叉树


if __name__ == "__main__":
    main()
