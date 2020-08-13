#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: is_cross.py
@Time: 2020/8/13 23:07
'''


"""
字符串的交错组成
三个字符串str1, str2, aim, aim中仅包含来自str1及str2的所有字符，且来自str1，str2的字符分别保持相对顺序
给定str1, str2, aim，判断这三个字符串是否满足上述条件

如str1="AB" str2="12"
aim= "A12B" "AB12" "A1B2"都满足条件
aim="BA12" "A2B1" 这样的不满足条件
"""

"""
生成dp布尔值矩阵，维度(M+1)*(N+1) M和N分别为str1和str2的长度，
dp[i][j]表示 aim[:i+j-1]能否被str1[:i-1] 和 str2[:j-1]交错组成
矩阵第一行：str1是空串，那么这一行的值取决于aim[:j-1]和str2[:j-1]是否相等；
矩阵第一列：str2是空串，那么这一列的值取决于aim[:i-1]和str1[:i-1]是否相等；
其他位置：
    - 如果dp[i-1][j]为true，意味着str1[:i-2] 和str2[:j-1]可以交错组成aim[:i+j-2]
    - 那么如果str1[i-1]和aim[i+j-1]相等，那么str1[:i-1] 和str2[:j-1]也可以交错组成aim[:i+j-1]
    - 如果dp[i][j-1]为true。。。一个意思
dp[i][j]只依赖于dp[i-1][j]和dp[i][j-1]，因此dp实际可用一维数组表示
"""

def is_crossed(str1: str, str2: str, aim: str) -> bool:
    if len(aim) != len(str1) + len(str2):
        return False
    dp = [False] * (len(str2) + 1)
    dp[0] = True
    for x in range(1, len(str2)+1):
        dp[x] = dp[x-1] and str2[x-1] == aim[x-1]
    for i in range(1, len(str1)+1):
        dp[0] = dp[0] and str1[i-1] == aim[i-1]
        for j in range(1, len(str2)+1):
            if (dp[j] and str1[i-1] == aim[i+j-1]) or (dp[j-1] and str2[j-1] == aim[i+j-1]):
                dp[j] = True
            else:
                dp[j] = False
    return dp[-1]

