#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: quicksort.py
@Time: 2020/9/22 16:48
'''
import random
from typing import List

"""
快速排序

分区
在一个数组中，选定一个随机索引index, 把比arr[index]大的数移到数组右边，比arr[index]小的数移到数组左边
执行完毕后，应有一个索引i, 使得数组arr[0...i-1]比arr[i]小，arr[i+1...len(arr)-1]比arr[i]大
然后再递归的对arr[0...i-1]和arr[i+1...len(arr)-1]执行相同操作
"""

def partition(arr, left, right):
    index = random.randint(left, right)
    pivot = arr[index]
    arr[index], arr[right] = arr[right], arr[index]
    small = left-1
    for i in range(left, right):
        if arr[i] < pivot:
            small += 1
            if i != small:
                arr[i], arr[small] = arr[small], arr[i]
    small += 1
    arr[right], arr[small] = arr[small], arr[right]

    return small

def quicksort(arr: List[int]):

    def process(arr, left, right):
        if left == right:
            return

        index = partition(arr, left, right)
        if index < right:
            process(arr, index+1, right)
        if index > left:
            process(arr, left, index-1)

    process(arr, 0, len(arr)-1)

arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
quicksort(arr)
print(arr)




