#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: num2alpha.py
@Time: 2020/8/17 20:36
'''

"""
有一个只包含数字的字符串s，这些数字可以转换为字母，规定"1"转换为"A", "2"转换为"B", ..., "26"转换为"Z"
求有多少中转换方式
如"1111"
1 1 1 1 -> AAAA
1 11 1 -> ALA
11 1 1 -> LAA
11 11 -> LL
1 1 11 -> AAL
一共有5种

设dp数组，长度就是字符串长度，dp[i]表示i+1位置的字符的组合数
那么：
如果s[i]可以和s[i-1]组合，依赖dp[i-2]
不和s[i-1]组合, s[i-1]，也可能是0
"""

def num2alpha(s: str) -> int:
    def isTrue(s):
        return 1 <= int(s) < 27 and not s.startswith("0")

    if s == "" or s.startswith("0"):
        return 0
    dp = [0] * len(s)
    dp[0] = 1
    if len(s) == 1:
        return dp[0]
    dp[1] += 1 if isTrue(s[:2]) else 0
    dp[1] += 1 if isTrue(s[1]) else 0

    for i in range(2, len(s)):
        combined = 0
        # 和前一个字符可以组合
        if isTrue(s[i-1:i+1]):
            combined = dp[i-2]
        # 不和前一个字符组合
        if isTrue(s[i]):
            not_combined = dp[i-1]
        else:
            not_combined = 0
        dp[i] = combined + not_combined
    return dp[-1]

