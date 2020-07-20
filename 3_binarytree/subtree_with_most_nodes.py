#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: subtree_with_most_nodes.py
@Time: 2020/7/20 20:29
'''
from mystruct.binarytree import BinaryTreeNode

"""
一颗二叉树中每个节点的值都不同，求包含最多节点的二叉搜索子树，并返回该树的根节点
采用后序遍历（左右根）的方式：
    1. 先看左子树，得到left_bst_size(左子树最大BST的节点数量)和left_bst_root(左子树最大BST的根节点)
    2. 再看右子树，得到right_bst_size(右子树最大BST的节点数量)和right_bst_root(右子树最大BST的根节点)
    3. 如果和left_bst_root和right_bst_root恰好是当前节点的左右子节点，且root.val >= root.left.val and root.val <= root.right.val
    ，返回和得到left_bst_size+right_bst_size+1 及root
    4. 如第三步条件不满足，则返回max(left_bst_size, right_bst_size) 及 left_bst_root和right_bst_root中拥有数量多的那个
"""


def subtree_most_nodes(root: BinaryTreeNode):
    # 后序遍历
    def postorder(root, max_size):
        if not root:
            return None, 0
        left_bst_root, left_bst_size = postorder(root.left, 0)
        right_bst_root, right_bst_size = postorder(root.right, 0)

        curr_bst_root, curr_bst_size = None, 0
        if root.left == left_bst_root and root.right == right_bst_root:
            if root.left and root.right:
                if root.val >= root.left.val and root.val <= root.right.val:
                    curr_bst_root, curr_bst_size = root, max(max_size, left_bst_size + right_bst_size + 1)
            elif root.left:
                if root.val >= root.left.val:
                    curr_bst_root, curr_bst_size = root, max(max_size, left_bst_root + 1)
            elif root.right:
                if root.val <= root.right.val:
                    curr_bst_root, curr_bst_size = root, max(max_size, right_bst_root + 1)
        elif left_bst_size > right_bst_size:
            curr_bst_root, curr_bst_size = left_bst_root, max(max_size, left_bst_size)
        else:
            curr_bst_root, curr_bst_size = right_bst_root, max(max_size, right_bst_size)

        return curr_bst_root, curr_bst_size

    return postorder(root, 0)[0]