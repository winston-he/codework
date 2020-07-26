#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: generate_bst.py
@Time: 2020/7/23 20:01
'''
from typing import List

from mystruct.binarytree import BinaryTreeNode, bfs, inorder_recursive

"""
已知一个有序数组sorted_arr没有重复值, 根据这个有序数组生成一棵平衡搜索二叉树

以中间结点作为根节点，递归求解即可
"""

def generate_bst(sorted_arr: List[int]) -> BinaryTreeNode:
    if len(sorted_arr) == 0:
        return
    mid = (len(sorted_arr)-1) // 2
    root = BinaryTreeNode(sorted_arr[mid])

    def inorder(sorted_arr, start, end, root, left=True):
        if end < start:
            return
        mid = (start + end) // 2
        if left:
            root.left = BinaryTreeNode(sorted_arr[mid])
            curr = root.left
        else:
            root.right = BinaryTreeNode(sorted_arr[mid])
            curr = root.right
        # 连接左子树
        inorder(sorted_arr, start, mid-1, curr, True)
        # 连接右子树
        inorder(sorted_arr, mid+1, end, curr, False)

    inorder(sorted_arr, 0, mid-1, root, True)
    inorder(sorted_arr, mid+1, len(sorted_arr)-1, root, False)
    return root

root = generate_bst([1,2,3,4,5,6,7,8,9])
bfs(root)
