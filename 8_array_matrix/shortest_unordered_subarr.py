#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: shortest_unordered_subarr.py
@Time: 2020/9/3 20:37
'''

"""
需要排序的最短子数组     
"""

from typing import List


def max_val(arr: List[int]) -> int:
    if len(arr) <= 1:
        return 0
    min_val = arr[-1]
    no_min_index = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > min_val:
            no_min_index = i
        else:
            min_val = arr[i]
    if no_min_index == -1:
        return 0
    max_val = arr[0]
    no_max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < max_val:
            no_max_index = i
        else:
            max_val = arr[i]
    return no_max_index - no_min_index + 1

