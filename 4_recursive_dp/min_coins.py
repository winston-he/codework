#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: min_coins.py
@Time: 2020/7/27 20:45
'''
from typing import List

"""
给定数组arr，arr中所有值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张。
再给定一个整数aim，代表总的钱数，求组成aim的最少货币数
"""


# 暴力法求解
# 最坏情况下，时间复杂度为O(aim^N)
def min_coins_enum(arr: List[int], aim: int):
    if not arr or aim < 0:
        return 0

    def process(arr, aim, index):
        res = 0
        if index == len(arr):
            res = 1 if aim == 0 else 0
        else:
            i = 0
            while arr[index] * i <= aim:
                res += process(arr, aim - arr[index] * i, index + 1)
                i += 1
        return res

    return process(arr, aim, 0)


def min_coins_dp(arr: List[int], aim: int):
    pass


print("暴力法求解，一共有{}种方法".format(min_coins_enum([5, 10, 25, 1], 1000)))
