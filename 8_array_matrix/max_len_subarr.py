#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_len_subarr.py
@Time: 2020/9/8 21:09
'''
from typing import List

"""
未排序正数数组中累加和为给定值的最长子数组长度
"""

def max_length(arr: List[int], target: int) -> int:
    if not arr or target <= 0:
        return 0

    left = right = 0
    res = arr[0]
    total = 0
    while right < len(arr):
        if total == target:
            res = max(res, right-left+1)
            total -= arr[left]
            left += 1
        elif total > target:
            total -= arr[left]
            left += 1
        else:
            right += 1
            if right < len(arr):
                total += arr[right]
    return res
