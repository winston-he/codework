#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: longest_common_series.py
@Time: 2020/8/5 20:11
'''


"""
给定两个字符串，求最长公共子序列
"""

def lcse(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return ''
    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

    if str1[0] in str2:
        for i in range(len(str2)):
            dp[0][i] = 1
    if str2[0] in str1:
        for i in range(len(str1)):
            dp[i][0] = 1

    for i in range(len(str1)):
        for j in range(len(str2)):
            curr_max = max(dp[i-1][j], dp[i][j-1])
            if str1[i] == str2[j]:
                curr_max = max(curr_max, dp[i-1][j-1]+1)
            dp[i][j] = curr_max

