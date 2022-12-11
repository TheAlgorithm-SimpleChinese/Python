# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 对称二叉树.py
@time: 2022/12/11 21:26
"""
# 题目链接：
"""
对称二叉树的判定条件是: 左子树的左孩子 == 右子树的右孩子 and 左子树的右孩子 == 右子树的左孩子
递归：
对于递归的终止条件：
    当两个节点都为空,进入下一循环;
    左右两个节点一个为空，一个不为空，一定不对称返回False;
    左右两个节点都不为空，值不相等，一定不对称返回False.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 左子树的左孩子==右子树的右孩子 and 左子树的右孩子 == 右子树的左孩子
        """
        递归,自定义函数
        """
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode):
        # 递归的终止条件是两个节点都为空
        # 或左右有任意一个不为空，一定不对称
        # 两个节点的值不相等
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)
