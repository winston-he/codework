#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_increase_sub.py
@Time: 2020/8/4 21:23
'''
from typing import List

"""
给定一个数组，求出这个数组的最长递增子序列
子序列可以是不连续的值
要使时间复杂度达到O(NlogN)
"""

"""
O(N^2)解法：
设长度为N的数组dp, dp[i]表示以索引i结尾的最长递增子序列的长度
找到dp[0...i-1]中的最大值，且如果这个位置上的值比arr[i]小，则dp[i] = dp[j]+1
初始状态dp[0] = 1
"""


def get_result(arr, dp):
    max_val, pos = 1, 0
    for i in range(1, len(dp)):
        if dp[i] > max_val:
            max_val = dp[i]
            pos = i
    curr_val = max_val - 1
    curr = arr[pos]
    res = [arr[pos]]
    for i in range(pos - 1, -1, -1):
        if curr_val == dp[i] and arr[i] < curr:
            res.append(arr[i])
            curr_val -= 1
            curr = arr[i]
    return res[::-1]


def get_max_increase_sub1(arr: List[int]):
    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return get_result(arr, dp)


"""
O(NlogN)解法: 二分查找
"""


def get_max_increase_sub2(arr: List[int]):
    ends = [0] * len(arr)
    ends[0], right = arr[0], 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        l, r = 0, right
        while l <= r:
            m = (l + r) // 2
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return get_result(arr, dp)


arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
print(get_max_increase_sub2(arr))
