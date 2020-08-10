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


def bfs(root: BinaryTreeNode):
    from collections import deque
    q = deque()
    q.append(root)
    while len(q):
        queue_len = len(q)
        while queue_len:
            curr = q.popleft()
            print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            queue_len -= 1

def inorder_recursive(root: BinaryTreeNode):
    if not root:
        return
    inorder_recursive(root.left)
    print(root.val)
    inorder_recursive(root.right)

def test_tree():
    root = BinaryTreeNode(5)
    root.left = BinaryTreeNode(3)
    root.right = BinaryTreeNode(7)
    root.left.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(4)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(8)
    # root.left.left.left = BinaryTreeNode(1)
    # root.left.left.right = BinaryTreeNode(9)

    # root.left.right.left = BinaryTreeNode(9)
    # root.left.right.right = BinaryTreeNode(10)
    # root.right.left.left = BinaryTreeNode(11)
    return root