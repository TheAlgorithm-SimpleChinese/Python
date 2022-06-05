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


"""
二叉树的遍历
"""


# 定义广度优先遍历(层次遍历)方法
def breadth_travel(tree: BiTNode):
    if tree is None:
        return
    else:
        # 仍然是用队列的方式实现遍历，末端按遍历顺序逐个添加节点，首端逐个弹出先读到的节点
        queue = [tree]
        while queue:
            cur = queue.pop(0)
            print(cur.data, end=" ")
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)


# 定义深度优先遍历中的先序遍历
def preorder(tree: BiTNode) -> None:
    if tree is None:
        return
    else:
        print(tree.data, end=" ")
        preorder(tree.lchild)
        preorder(tree.rchild)


# 定义深度优先遍历中的中序遍历
def inorder(tree: BiTNode) -> None:
    if tree:
        inorder(tree.lchild)
        print(tree.data, end=" ")
        inorder(tree.rchild)


# 定义深度优先遍历中的后序遍历
def postorder(tree: BiTNode) -> None:
    if tree is None:
        return
    else:
        postorder(tree.lchild)
        postorder(tree.rchild)
        print(tree.data, end=" ")


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
    preorder(tree)  # 前序遍历
    print("\n")
    inorder(tree)  # 中序遍历
    print("\n")
    postorder(tree)  # 后续遍历
    print("\n")
    breadth_travel(tree)  # 层次遍历


if __name__ == "__main__":
    main()
