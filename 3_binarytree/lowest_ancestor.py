#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: lowest_ancestor.py
@Time: 2020/7/24 22:48
'''
from mystruct.binarytree import BinaryTreeNode, test_tree

"""
在二叉树中找到两个节点的最低公共祖先

如果希望减少单次查询的时间，可以牺牲O(N)的空间，使时间复杂度变成O(logN)
使用哈希表，key代表每一个节点，value代表这个节点的父节点
对节点a，可以得出它的父节点集合
然后不断往上查找b的父节点，直到在a的父节点集合中找到这个节点，就是a，b的最低公共祖先
    - 先序遍历构建哈希表
"""

def lowest_ancestor(root: BinaryTreeNode, a: BinaryTreeNode, b: BinaryTreeNode):
    if not root or root == a or root == b:
        return root

    left = lowest_ancestor(root.left, a, b)
    right = lowest_ancestor(root.right, a, b)
    if left and right:
        return root
    return left if left else right


root = test_tree()

a = root.left.left.left
b = root.left.right

print(lowest_ancestor(root, a, b).val)