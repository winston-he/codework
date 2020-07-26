#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_distance.py
@Time: 2020/7/24 23:29
'''
from typing import Tuple

from mystruct.binarytree import BinaryTreeNode, test_tree

"""
二叉树上两节点的最大距离（两个节点间的距离指的是两个节点的路径上节点总数）
答案可能是：
    - 左子树的节点最大距离
    - 右子树的节点最大距离
    - left_height + right_height + 1

"""


def max_distance(root: BinaryTreeNode) -> Tuple[int, int]:
    if not root:
        return 0, 0
    left_height, left_dist = max_distance(root.left)
    right_height, right_dist = max_distance(root.right)

    # 树的高度应该是左右子树更高者+1
    height = max(left_height, right_height) + 1
    distance = max(left_height + right_height + 1, left_dist, right_dist)

    return height, distance

root = test_tree()

print(max_distance(root)[1])
