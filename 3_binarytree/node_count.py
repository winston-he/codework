#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: node_count.py
@Time: 2020/7/27 19:53
'''
from mystruct.binarytree import BinaryTreeNode, test_tree

"""
给定一棵完全二叉树，返回它的节点数

1. 先找到整棵树的最左节点，这样可以确定整棵树的层数H
2. 递归过程：
    （1）如果当前节点是node，查看node的右子节点，找到右子节点的最左子节点，
        -> 如果最左子节点的深度就是H，那么说明node的整棵左子树是满二叉树，用公式求其节点数；
            -> 然后对右子树递归求解
        -> 如果最左子节点的深度不是H，那么说明node的整棵右子树是满二叉树，用公式求其节点数；
            -> 然后对左子树递归求解
"""

def get_node_count(root: BinaryTreeNode) -> int:
    if not root:
        return 0

    # 先求树的高度
    curr = root
    level = 1
    while curr.left:
        level += 1
        curr = curr.left

    def process(root, level, curr_depth):
        if not root:
            return 0
        if not root.right:
            return process(root.left, level, curr_depth+1) + 1
        curr, depth = root.right, 1
        while curr.left:
            depth += 1
            curr = curr.left
        if curr_depth + depth == level:
            return 2**depth + process(root.right, level, curr_depth+1)
        else:
            return 2**depth + process(root.left, level, curr_depth+1)
    return process(root, level, 1)


root = test_tree()

print("Total node count is: ", get_node_count(root))

