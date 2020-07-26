#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: tree_contains.py
@Time: 2020/7/22 20:14
'''
from mystruct.binarytree import BinaryTreeNode

"""
给定两棵二叉树t1, t2, 判断t1是否包含t2的全部拓扑结构
"""


def is_contained(t1: BinaryTreeNode, t2: BinaryTreeNode) -> bool:
    def check(t1, t2):
        if not t2:
            return True
        if not t1 or t1.val != t2.val:
            return False
        return check(t1.left, t2.left) and check(t1.right, t2.right)
    if not t1:
        return False
    if not t2:
        return True
    return check(t1, t2) or is_contained(t1.left, t2.left) or is_contained(t1.right, t2.right)
