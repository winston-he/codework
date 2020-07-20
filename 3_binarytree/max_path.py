#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_path.py
@Time: 2020/7/20 19:52
'''
from mystruct.binarytree import BinaryTreeNode

"""
在二叉树中找到累加和为指定值的最长路径长度

给定二叉树的root，及整数k，求二叉树中累加和为k的最长路径（路径不一定经过根节点）
时间复杂度为O(n), 空间复杂度为O(h)
使用一个字典d，key表示累加和，value表示得到这个累加和的最小层数；
给定d一个初始值(0, 0)，代表累加到第0层时和为0
"""

def max_path(root: BinaryTreeNode, k: int) -> int:
    d = dict({0: 0})

    # 先序遍历
    def process(root, level, curr_sum, k, max_len, map):
        if not root:
            return max_len
        curr_sum = root.val + curr_sum
        if curr_sum not in map.keys():
            map[curr_sum] = level
        if curr_sum - k in map.keys():
            max_len = max(max_len, level - map[curr_sum-k])
        if root.left:
            process(root.left, level+1, curr_sum, k, max_len, map)
        if root.right:
            process(root.right, level+1, curr_sum, k, max_len, map)
        # ??
        if level == map[curr_sum]:
            del map['curr_sum']

        return max_len
    return process(root, 1, 0, k, 0, d)
