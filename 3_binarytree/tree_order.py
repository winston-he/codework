#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: tree_order.py
@Time: 2020/7/15 20:43
'''

from mystruct.binarytree import BinaryTreeNode
from mystruct.stack import Stack

def foo(tree_node: BinaryTreeNode):
    print(tree_node.val)


# 递归实现二叉树的先序遍历(根左右)
def preorder_recursive(root: BinaryTreeNode):
    if not root:
        return
    foo(root.val)
    preorder_recursive(root.left)
    preorder_recursive(root.right)


# 递归实现二叉树的中序遍历(左根右)
def inorder_recursive(root: BinaryTreeNode):
    if not root:
        return
    inorder_recursive(root.left)
    foo(root)
    inorder_recursive(root.right)


# 递归实现二叉树的后序遍历(左右根)
def postorder_recursive(root: BinaryTreeNode):
    if not root:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    foo(root)

# 循环+栈实现二叉树的先序遍历
def preorder_iter(root: BinaryTreeNode):
    s = Stack()
    # 每次打印栈顶，并将栈顶的右孩子先入栈（如果有的话），再将左孩子入栈（如果有的话）
    if not root:
        return
    s.push(root)
    while not s.empty():
        foo(s.pop())
        if root.right:
            s.push(root.right)
        if root.left:
            s.push(root.left)

"""
1. 不断将左边界入栈
2. 当栈顶不在有左孩子时，弹出栈顶并打印；将栈顶的右孩子入栈（如果有的话）
3. 重复步骤1（将左边界入栈）
"""
def inorder_iter(root: BinaryTreeNode):
    if not root:
        return
    s = Stack()
    while not s.empty() or root:
        if root:
            s.push(root)
            root = root.left
        else:
            root = s.pop()
            foo(root)
            root = root.right


