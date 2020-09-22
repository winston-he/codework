#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: insertionsort.py
@Time: 2020/9/22 15:26
'''
import random
from typing import List

"""
插入排序
以升序排序为例
假定arr[0...i]是一个排序序列，为arr[j](i<j<len(arr))找到合适的位置，“插入”到arr[0...i]中
对于基本有序的序列，插入排序有较高的效率
"""

def insertsort(arr: List[int]):
    for i in range(len(arr)-1):
        a, b = i, i + 1
        while a >= 0 and arr[b] < arr[a]:
            arr[b], arr[a] = arr[a], arr[b]
            b -= 1
            a -= 1

# arr = [random.randint(0, 100) for _ in range(10)]
# print(arr)
# insertsort(arr)
# print(arr)

