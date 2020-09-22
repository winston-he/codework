#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: mergesort.py
@Time: 2020/9/22 16:34
'''
import random
from typing import List

"""
归并排序
把原数组以中间索引为界切分成两个数组，再切分。。
直至数组中只有一个元素，这时合并相邻的元素，返回。。
递归的每一层，都是在合并两个有序的数组
"""

def merge(arr_1, arr_2):
    """
    把两个有序的数组合并成一个有序的数组
    """
    res = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            res.append(arr_1[i])
            i += 1
        else:
            res.append(arr_2[j])
            j += 1
    while i < len(arr_1):
        res.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        res.append(arr_2[j])
        j += 1
    return res

def mergesort(arr: List[int]):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergesort(left), mergesort(right))

arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
arr = mergesort(arr)
print(arr)