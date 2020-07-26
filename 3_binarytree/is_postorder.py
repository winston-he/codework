#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: is_postorder.py
@Time: 2020/7/22 20:40
'''
from typing import List

from mystruct.binarytree import BinaryTreeNode

"""
判断一个序列(在这个序列中没有重复值)是否为一棵搜索二叉树后序遍历的结果
对于搜索二叉树的后序遍历序列，序列最后一个元素就是根节点，序列的左半部是其左子树（全部小于根），右半部是其右子树（全部大于根）
"""

def is_postorder(arr: List[int]) -> bool:
    if len(arr) == 0:
        return False

    def is_postorder_recursive(arr, start, end):
        if start == end:
            return True
        root = arr[end]
        left_end = start
        while left_end < end and arr[left_end] < root:
            left_end += 1
        left_end -= 1
        tmp = left_end + 1
        # 找到了左子树的末尾，即left_end，此时索引从left_end+1一直到end-1之间, 不应再出现比root小的值
        while tmp < end:
            if arr[tmp] < root:
                return False
        
        # 再分别判断左右子树是否符合
        return is_postorder_recursive(arr, start, left_end) and is_postorder_recursive(arr, left_end+1, end-1)

    return is_postorder_recursive(arr, 0, len(arr)-1)