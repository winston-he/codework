#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: error_tree.py
@Time: 2020/7/21 20:48
'''
from mystruct.binarytree import BinaryTreeNode, test_tree

"""
一棵树原本是搜索二叉树，因为两个节点位置错误而使它不再是搜索二叉树（这棵树中所有值都不相等）

一棵BST的中序遍历就是一个升序序列，假如这个升序序列是1,2,3,4,5
发生错误有两种可能:
    1. 两个错误的节点在中序序列中相邻：1,3,2,4,5, 则在这个序列中有一组降序子序列，降序对的两个元素就是错误节点
    2. 两个错误的节点在中序序列中不相邻：1,5,3,4,2 则这个序列中有两组降序子序列错误节点分别是两个降序对的第1，第2个元素
"""


def get_error_nodes(root: BinaryTreeNode):
    err_count, l, res = 0, [], []

    def inorder(root, l, res):
        if not root:
            return
        if root.left:
            inorder(root.left, l, res)
        if len(l) and root.val < l[-1].val:
            res += [l[-1], root]
        l.append(root)
        if root.right:
            inorder(root.right, l, res)
    inorder(root, l, res)

    if len(res) == 2:
        return tuple(res)
    else:
        return res[0], res[-1]


root = test_tree()
res = get_error_nodes(root)
for r in res:
    print(r.val)