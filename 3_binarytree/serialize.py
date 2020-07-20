#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: serialize.py
@Time: 2020/7/16 20:47
'''

"""
二叉树的序列化和反序列化
序列化即将二叉树转换为可存入文件的格式，反序列化即将文件读出转换成二叉树

序列化：将二叉树转换成字符串，反序列化：将字符串转换成二叉树
每个节点后用!隔开，空节点用#表示
使用先序遍历（递归）或层遍历（队列、广度优先搜索）
"""

from mystruct.binarytree import BinaryTreeNode, test_tree


def serialize_tree_preorder(root: BinaryTreeNode):
    if not root:
        return
    s = ''

    def process(root, s):
        s += str(root.val) + '!'
        if root.left:
            s = process(root.left, s)
        else:
            if root.right:
                s += "#!"
        if root.right:
            s = process(root.right, s)
        else:
            if root.left:
                s += "#!"
        return s
    return process(root, s)


def serialize_tree_level(root: BinaryTreeNode):
    from collections import deque
    if not root:
        return

    q = deque()
    q.append(root)
    s = ""
    while len(q):
        len_q = len(q)
        while len_q:
            curr = q.popleft()
            s += str(curr.val) + "!"
            if curr.left:
                q.append(curr.left)
            else:
                if curr.right:
                    q.append(BinaryTreeNode("#"))
            if curr.right:
                q.append(curr.right)
            else:
                if curr.left:
                    q.append(BinaryTreeNode("#"))
            len_q -= 1
    return s

root = test_tree()
print(serialize_tree_preorder(root))

# 先序序列的反序列化：使用队列

# 层遍历序列的反序列化：使用队列