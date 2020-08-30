#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: split_string_palindrome.py
@Time: 2020/8/30 19:23
'''
from pprint import pprint

"""
把一个字符串切割成若干子串，使这些子串都是回文，求最少需要切割几次
如果这个字符串本身就是回文，则不用切割，返回0
"""

# ACDCDCDAD
def split_string(s: str) -> int:
    is_palin = [[False for _ in range(len(s))] for _ in range(len(s))]
    # 初始化为无穷大
    dp = [float("inf")] * (len(s)+1)
    dp[0] = -1

    for i in range(1, len(s)+1):
        for j in range(1, i+1):
            # s[i..j]为回文的条件
            # 1. 长度为1
            # 2. 长度为2且两个字符相等
            # 3. 长度大于等于2且is_palin[i-1][j+1]且两端字符相等
            if j == i or (j == i-1 and s[i-1] == s[j-1]) or (i-j >= 2 and is_palin[i-2][j] and s[i-1] == s[j-1]):
                is_palin[i-1][j-1] = True
                dp[i] = min(dp[i], dp[j-1] + 1)
    return dp[-1]
