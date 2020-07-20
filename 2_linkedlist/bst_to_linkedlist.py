#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: bst_to_linkedlist.py
@Time: 2020/7/9 19:32
'''

"""
将二叉搜索树转换为有序的双向链表
"""

"""
对BST进行有序的遍历，就是中序遍历
"""


# 方法1：将节点逐个放入队列，并逐个出列然后重新连接
def in_order_put_queue(root, q):
    if not root:
        return
    in_order_put_queue(root.left, q)
    q.append(root)
    in_order_put_queue(root.right, q)


def bts_to_linkedlist_q(root):
    from collections import deque
    q = deque()
    in_order_put_queue(root, q)
    head = q[0]
    while len(q):
        curr = q.pop()
        if len(q):
            curr.right = q[-1]
            q[-1].left = curr
        else:
            curr.right = None

    return head


# 方法2：递归
def bts_to_linkedlist_recursive(root):
    if not root:
        return

    def process(root):
        left_head, left_tail = process(root.left) if root.left else None, None
        right_head, right_tail = process(root.right) if root.right else None, None
        head = tail = root
        if left_head:
            head = left_head
            left_tail.right = root
            root.left = left_tail
            tail = root
        if right_head:
            root.right = right_head
            right_head.left = root
            tail = right_tail
        return head, tail

    return process(root)[0]
