#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: str_replace.py
@Time: 2020/8/24 20:36
'''
from typing import List

"""
给定字符数组arr, 其中左半区没有None, 右半区全是None（假设右半区空间足够多）, 将左半区的空格字符" "替换成"%20"
["a", " ", "b", None, None, None] -> ["a", "%", "2", "0", "b", None]
原地替换
"""

"""
1. 先遍历一遍，数一下有多少空格字符
2. 假设有m个空格，则需要的额外空间是2*m
"""

def replace(arr: List[str]) -> None:
    space_count = end = 0
    while arr[end] is not None:
        if arr[end] == " ":
            space_count += 1
        end += 1
    pos = end + 2 * space_count
    for i in range(end, -1, -1):
        if arr[i] == " ":
            arr[pos] = "0"
            arr[pos-1] = "2"
            arr[pos-2] = "%"
            pos -= 3
        else:
            arr[pos] = arr[i]
            pos -= 1
arr = [" ", "a", " ", " ", "b", "b", " ", "p", " "]
arr += [None] * 100
replace(arr)
print(arr)