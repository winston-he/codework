#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: mostEOR.py
@Time: 2020/8/10 20:35
'''
from typing import List

"""
子数组异或和的最多划分

把一个整数数组（可能有正数、负数、零）切分为若干个子数组，设所有子数组中，异或和为0的子数组的个数为M。求：M的最大值

须使时间复杂度为O(N)

思路：
设原数组为arr
设dp数组，dp[i]为：arr[:i+1]这个数组中子数组的最大数量，那么推导得到dp[N-1]就是最终答案
推算dp[i]时，分两种情况讨论：
    (1) arr[i]属于的子数组异或和不为0
        - 这种情况下: dp[i] = dp[i-1]
    (2) arr[i]属于的子数组异或和为0
        - 如果arr[i]所在的这个子数组是arr[k:i+1] (k位置是这个异或和为0的子数组的开始索引)
        - 那么arr[k-1]就是上一个子数组的结束位置，所以dp[i] = dp[k-1] + 1
        - 因为一个数和0的异或结果还是这个数，所以：
            - 当arr[:k-1]的异或和等于arr[:i]的异或和时，此时的k就是我们要找的位置，可以拿一个哈希表来记录arr[:i]的异或和
    (3) 要用到一个哈希表，以及dp数组，因此空间复杂度O(N)
"""


def most_eor(arr: List[int]) -> int:
    if arr is None or len(arr) == 0:
        return 0
    dp = [0] * len(arr)
    eor_dict, eor = dict(**{0: -1}), 0
    dp[0] = 1 if arr[0] == 0 else 0
    for i, n in enumerate(arr):
        eor ^= n
        if eor in eor_dict.keys():
            k = eor_dict[eor]
            dp[i] = dp[k] + 1 if k != -1 else 1
        dp[i] = max(dp[i], dp[i - 1])
        eor_dict[eor] = i
    return dp[-1]
