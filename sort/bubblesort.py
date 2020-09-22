#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: bubblesort.py
@Time: 2020/9/22 15:04
'''
import random
from typing import List

"""
冒泡排序：
以升序排序为例，
每一趟比较相邻的两个元素，并使较大的元素往右“冒”
"""

def bubblesort(arr: List[int]):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
bubblesort(arr)
print(arr)