#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: selectionsort.py
@Time: 2020/9/22 15:18
'''
import random
from typing import List

"""
选择排序：
以升序排序为例，
每一趟，找到当前最小的元素放在最前面
"""


def selectionsort(arr: List[int]):
    for i in range(len(arr)):
        curr, k = arr[i], i
        for j in range(i + 1, len(arr)):
            if arr[j] < curr:
                curr = arr[j]
                k = j
        arr[i], arr[k] = arr[k], arr[i]


arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
selectionsort(arr)
print(arr)
