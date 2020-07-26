#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: print_by_level.py
@Time: 2020/7/21 19:29
'''
from mystruct.binarytree import BinaryTreeNode, test_tree

"""
将二叉树按层打印（广度优先遍历）
如：
    一个数组[1,2,3,4,5,6,7], 它按层的方式表达一棵完全二叉树，打印结果为：
Level 1: 1
Level 2: 2 3
Level 3: 4 5 6 7
"""

from collections import deque

def print_by_level(root: BinaryTreeNode):
    if not root:
        return
    q = deque()
    q.append(root)
    last, next_last, level = root, None, 1
    text = 'Level {}:'.format(level)
    while len(q):
        queue_len = len(q)
        while queue_len > 0:
            curr = q.popleft()
            text += ' ' + str(curr.val)
            # 每一次都将next_last更新为当前能找到的下一层最右边的一个
            if curr.left:
                q.append(curr.left)
                next_last = curr.left
            if curr.right:
                q.append(curr.right)
                next_last = curr.right
            # 如果是当前行的最后一个
            if curr == last:
                print(text)
                level += 1
                text = 'Level {}:'.format(level)
                last = next_last
            queue_len -= 1

root = test_tree()
print_by_level(root)