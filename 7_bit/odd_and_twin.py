#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: odd_and_twin.py
@Time: 2020/9/2 22:38
'''
from typing import List

"""
一个数组中，有两个数字出现了奇数次，其他数字都出现了偶数次，找出这两个数
"""


def find_odds(nums: List[int]):
    res = 0
    for n in nums:
        res ^= n
    ans_1 = ans_2 = 0
    count = 0
    while res & 0b1 != 1:
        res >>= 1
        count += 1
    for n in nums:
        if n & (1 << count) == 0:
            ans_1 ^= n
        else:
            ans_2 ^= n
    return ans_1, ans_2
