#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: get_next_node.py
@Time: 2020/7/23 20:31
'''
from mystruct.binarytree import BinaryTreeNode

"""
假设一种二叉树节点，除了指向左右子节点的指针外，还有指向父节点的parent指针，
给定一个节点，求这个节点在二叉树中的后继节点
后继节点指的是一个节点在中序遍历中的后一个节点

如果目标节点为node：
    1. 如果node有右子树，则后继节点是右子树的最左的节点
    2. 如果node没有右子树：
        (1) 如果node是左子节点，则其父节点就是它的后继节点
        (2) 如果node是右子节点，则不断往上找，直到有一个祖先是其父节点的左子节点，那么这个父节点就是node的后继节点
分以上三种情况讨论 
"""

class BinaryTreeNodeWithParentPtr(BinaryTreeNode):
    def __init__(self, val):
        super().__init__(val)
        self.parent = None


def get_next_node(node: BinaryTreeNodeWithParentPtr):
    # 有右子树
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    # 如果是根节点
    if not node.parent:
        return None

    # 没有右子树，是左子节点
    if node.parent.left == node:
        return node.parent

    # 没有右子树，是右子节点
    curr = node
    while curr.parent and curr == curr.parent.right:
        curr = curr.parent
    return curr.parent

