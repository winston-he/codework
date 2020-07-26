#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: is_BST.py
@Time: 2020/7/22 21:09
'''

# 判断一棵二叉树是否为搜索二叉树
from collections import deque

from mystruct.binarytree import BinaryTreeNode, test_tree


def is_bst(root: BinaryTreeNode) -> bool:
    if not root:
        return True
    left = True if not root.left else root.left.val <= root.val
    right = True if not root.right else root.right.val >= root.val
    return left and right and is_bst(root.left) and is_bst(root.right)


# 判断一棵树是否为完全二叉树
# 完全二叉树：Complete Binary Tree (CBT)
# 广度优先遍历

def is_cbt(root: BinaryTreeNode) -> bool:
    if not root:
        return False
    last, next_last, is_leaf, find_null = root, None, True, False
    q = deque()
    q.append(root)
    while len(q):
        queue_len = len(q)
        while queue_len:
            curr = q.popleft()
            # 只要有一个孩子节点，就说明当前层不是叶子层
            if curr.left or curr.right:
                is_leaf = False
            # 如果发生这种情况马上返回False:
            # 如果没有左但有右
            # 当前层有null节点，但是当前层不是叶子层

            if curr.left:
                if find_null:
                    return False
                q.append(curr.left)
                next_last = curr.left
            if curr.right:
                if find_null:
                    return False
                q.append(curr.right)
                next_last = curr.right
            if not curr.left or not curr.right:
                find_null = True
            if (not curr.left and curr.right) or (find_null and not is_leaf):
                return False
            # 换行
            if curr == last:
                last = next_last
                find_null = False
                is_leaf = True
            queue_len -= 1
    return True


root = test_tree()
print(is_cbt(root))
