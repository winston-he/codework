#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: binary_search.py
@Time: 2020/8/24 20:15
'''
from typing import List

"""
给定一个字符串数组，其中的字符串是按字典顺序由小到大排列的，但有些位置上是None，
给定一个字符串，返回这个字符串在数组中的最左索引
"""

"""
二分查找：
1. 令start = 0, end = len(arr)-1
2. 令mid = (start+end) // 2
3. 如果arr[mid] = target, 继续在左半区查找
4. 如果arr[mid] > target, 继续在左半区查找；如果arr[mid] < target, 继续在右半区查找
5. 如果arr[mid] is None, 线性搜索左半区，找到第一个不为None的值，从步骤3继续；如果左半区全为None，则在右半区中查找
"""

def binary_search(arr: List[str], target) -> int:
    if not target or not arr:
        return -1
    start, end = 0, len(arr)-1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            res = mid
            end = mid - 1
        elif arr[mid] is not None and arr[mid] > target:
            end = mid - 1
        elif arr[mid] is not None and arr[mid] < target:
            start = mid + 1
        else:
            tmp = mid - 1
            while tmp >= 0 and arr[tmp] is None:
                tmp -= 1
            if tmp == -1:
                start = mid + 1
            else:
                if arr[tmp] > target:
                    end = tmp - 1
                elif arr[tmp] < target:
                    start = mid + 1
                else:
                    res = tmp
                    end = tmp - 1
    return res


# print(binary_search([None, "a", None, "a", None, "b", None, "f"], "d"))

print(binary_search([None, "a", "d", "d", "d", "e"], "d"))