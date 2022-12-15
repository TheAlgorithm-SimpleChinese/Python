# -*- coding: utf-8 -*-
"""
@author: liuyang
@software: PyCharm
@file: 二叉树的最大深度.py
@time: 2022/12/13 15:03
"""
# 题目链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/?favorite=2cktkvj
"""
解题思路：
递归法，我以自底向上，即后序遍历的方式为例，解决本题，因为这相比而言，更好理解。

既然是用递归法，那还是按照往常，祭出递归二步曲：

(1) 找出重复的子问题。

后序遍历的顺序是：左子树、右子树、根。

在本题同样也是这个顺序：递归左子树的最大高度，递归右子树的最大高度，求根的最大高度。

对于左子树和右子树来说，也都是同样的操作。

(2) 确定终止条件。

对于二叉树的遍历来说，想终止，即没东西遍历了，没东西遍历自然就停下来了。

那就是当前的节点是空的，既然是空的那就没啥好遍历。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 节点为空，高度为 0
        if root is None:
            return 0

        # 递归计算左子树的最大深度
        leftHeight = self.maxDepth(root.left)
        # 递归计算右子树的最大深度
        rightHeight = self.maxDepth(root.right)

        # 二叉树的最大深度 = 子树的最大深度 + 1（1 是根节点）
        return max(leftHeight, rightHeight) + 1
