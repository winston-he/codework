#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: binarytree.py
@Time: 2020/7/15 20:44
'''
import random


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def random_binary_tree(level: int, val_range=(0, 20)):
    """
    生成一颗随机的二叉树
    :param level: 树的高度
    :param val_range: 节点的取值范围
    :return:
    """
    empty_layer = True
    root = BinaryTreeNode(random.randint(val_range))

    def preorder(root):
        pass
    return root

def random_complete_binary_tree():
    pass

def random_full_binary_tree():
    pass


def test_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.right = BinaryTreeNode(8)
    return root
