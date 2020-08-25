#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: min_distance.py
@Time: 2020/8/25 21:13
'''
from typing import List

"""
数组中两个字符串的最小距离
给定一个字符串数组以及两个字符串s1, s2,
求s1, s2在数组中的最小距离（索引的最小差值）
"""

"""

"""

def min_distance(strings: List[str], s1: str, s2: str) -> int:
    res = float("inf")
    index1 = index2 = -1
    for i, s in enumerate(strings):
        if s == s1:
            if index2 != -1:
                res = min(res, i - index2)
            index1 = i
        if s == s2 and index1 != -1:
            if index1 != -1:
                res = min(res, i - index1)
            index2 = i
    return res if res < float("inf") else -1

