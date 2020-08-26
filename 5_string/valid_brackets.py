#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: valid_brackets.py
@Time: 2020/8/26 20:28
'''
"""
括号字符串的有效性和最长有效长度
1. 给定一个字符串，判断是不是整体有效的括号字符串
    - 字符串中只能有"("或")", 因此如果出现别的字符串，就返回False
    - 每次遍历，"("的数量都应大于等于")"的数量
"""
def valid_brackets(s: str) -> bool:
    a = b = 0
    for c in s:
        if c not in ("(", ")"):
            return False
        if c == "(":
            a += 1
        else:
            b += 1
        if b > a:
            return False
    return True

"""
给定一个括号字符串, 返回最长的有效括号字符串
建立长度为n的dp数组，dp[i]表示必须以s[i]结尾的字符串中有效括号字符串的最大长度
1. 对于字符串"(()())", 当遍历到最后一个字符时，设此时位置为i
    - dp[i-1]表示以前一个字符结尾的有效括号字符串的最大长度，那么str[i-dp[i-1]-1]就是这段字符串的前一个字符
    - 如果str[i-dp[i-1]-1]为"(", 那么str[i-dp[i-1]-1]恰好构成一对括号；
    - 那么此时dp[i] = dp[i-1] + 2;
    - 同时，还要再加上dp[i-dp[i-1]-2]，所以此时dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
    - 当然，这里面用到的索引都必须为正数。
"""
def max_valid_brackets(s: str) -> int:
    dp = [0] * len(s)
    res = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            pre = i - dp[i-1] - 1
            if pre >= 0 and s[pre] == '(':
                dp[i] = dp[i-1] + 2
                if pre - 1 >= 0:
                    dp[i] += dp[pre-1]
        res = max(res, dp[i])
    return res
