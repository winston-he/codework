#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: print_zigzag.py
@Time: 2020/7/21 19:31
'''
from collections import deque

from mystruct.binarytree import BinaryTreeNode, test_tree

"""
将二叉树按层zigzag的方式(S型)打印
如：
    一个数组[1,2,3,4,5,6,7], 它按层的方式表达一棵完全二叉树，打印结果为：
Level 1 from left to right: 1
Level 2 from right to left: 3 2
Level 3 from left to right: 4 5 6 7

如果是从左到右，一律从queue头部弹出节点，左、右孩子从尾部进入队列
如果是从右到左，一律从queue尾部弹出节点，右、左孩子从头部进入队列
"""


def print_zigzag(root: BinaryTreeNode):
    if not root:
        return
    q = deque()
    q.append(root)
    left_to_right = True
    last, next_last, level = root, None, 1
    text = "Level {} from left to right:".format(level)
    while len(q):
        queue_len = len(q)
        while queue_len:
            curr = q.popleft() if left_to_right else q.pop()
            text += ' ' + str(curr.val)
            # 如果从做到右
            if left_to_right:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    next_last = curr.right
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    next_last = curr.left
            else:
                if curr.right:
                    q.appendleft(curr.right)
                if curr.left:
                    next_last = curr.left
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    next_last = curr.right

            # 一行到了末尾
            if curr == last:
                print(text)
                level += 1
                text = "Level {} from left to right:".format(level) if not left_to_right else \
                    "Level {} from right to left:".format(level)
                last = next_last
                left_to_right = not left_to_right
            queue_len -= 1

root = test_tree()
print_zigzag(root)
