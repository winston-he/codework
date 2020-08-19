#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: is_deformation.py
@Time: 2020/8/19 19:47
'''

"""
字符串是否为变形词
如果两个字符串具有相同种类的字符且每个字符出现的次数一样，则两个字符串互为变形词
"""

"""
哈希表

时间复杂度：O(max{M, N})
空间复杂度：O(max{M, N})
"""
from collections import defaultdict


def is_deformation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    d = defaultdict(int)
    for c in s1:
        d[c] += 1
    for c in s2:
        d[c] -= 1
        if d[c] < 0:
            return False
    return True
