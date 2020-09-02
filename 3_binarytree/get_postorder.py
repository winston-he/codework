#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: get_postorder.py
@Time: 2020/7/26 13:05
'''
from typing import List

"""
根据二叉树的先序遍历和中序遍历数组得到后序遍历数组

借助一个字典d存储中序序列：key为节点的值，value为节点索引
"""


def get_postorder_array(preorder: List[int], inorder: List[int]):
    postorder = [0] * len(preorder)
    d = dict()
    for i, n in enumerate(inorder):
        d[n] = i

    def process(pre_arr, pre_start, pre_end,  # 先序数组/起始位置/结束位置
                in_arr, in_start, in_end,  # 中序数组/起始位置/结束位置
                post_arr,  # 结果数组
                pos,  # 当前应填充的位置
                map):  # 中序序列字典
        if pos < 0:
            return pos
        root = pre_arr[pre_start]
        post_arr[pos] = root
        in_pos = map[root]
        pos -= 1
        left_tree_len = in_pos - in_start
        new_pre_end = pre_start + left_tree_len
        new_pos = process(pre_arr, pre_start + 1, new_pre_end,
                          in_arr, in_start, in_pos - 1,
                          post_arr,
                          pos,
                          map)
        return process(pre_arr, new_pre_end + 1, pre_end,
                       in_arr, in_pos + 1, in_end,
                       post_arr,
                       new_pos,
                       map)
    process(preorder, 0, len(preorder) - 1,
            inorder, 0, len(inorder) - 1,
            postorder,
            len(preorder) - 1,
            d)

    return postorder


print(get_postorder_array([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))
