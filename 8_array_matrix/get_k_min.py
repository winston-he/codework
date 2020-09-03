#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: get_k_min.py
@Time: 2020/9/3 20:13
'''
import random
from heapq import nsmallest
from typing import List

"""
找到无序数组中最小的k个数

大根堆
"""


def heapify(nums: List[int], index: int, heap_size: int):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    while left < heap_size:
        if nums[left] > nums[index]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != index:
            nums[largest], nums[index] = nums[index], nums[largest]
        else:
            break
        index = largest
        left = index * 2 + 1
        right = index * 2 + 2


def heap_insert(nums: List[int], value: int, index: int):
    nums[index] = value
    while index != 0:
        parent = (index - 1) // 2
        if nums[parent] < nums[index]:
            nums[parent], nums[index] = nums[index], nums[parent]
            index = parent
        else:
            break


def get_k_min(nums: List[int], k) -> List[int]:
    res = [0] * k
    for i in range(k):
        heap_insert(res, nums[i], i)
    for i in range(k, len(nums)):
        if nums[i] < res[0]:
            res[0] = nums[i]
            heapify(res, 0, k)
    return res
