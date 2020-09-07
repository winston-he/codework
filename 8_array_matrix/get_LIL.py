#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: get_LIL.py
@Time: 2020/9/7 19:42
'''
from typing import List


"""
可整合数组：
如果一个数组中两个相邻的数的差值是1，则此数组为可整合数组
"""

"""
解法：
- 遍历所有子数组（O(N^2)）
- 判断每一个子数组是否为可整合数组，需要符合以下两个条件
    - 是否没有重复的数 max(sub_arr)-min(sub_arr) + 1 == len(sub_arr)
    - (max(sub_arr) + min(sub_arr)) * len(sub_arr) // 2 == sum(sub_arr)
"""

def get_LIL(arr: List[int]):
    res = 0
    for i in range(len(arr)-1):
        min_val = max_val = total = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] > max_val:
                max_val = arr[j]
            if arr[j] < min_val:
                min_val = arr[j]
            total += arr[j]
            if max_val-min_val+1 == j-i+1 and (max_val+min_val)*(j-i+1)//2 == total:
                res = max(res, j-i+1)
    return res
