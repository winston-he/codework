#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: sort_num.py
@Time: 2020/9/5 15:45
'''
from random import shuffle
from typing import List

"""
自然数数组的排序
"""


def sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        while arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]


arr = list(range(1, 20))
shuffle(arr)
sort(arr)
