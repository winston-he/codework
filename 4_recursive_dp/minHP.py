#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: minHP.py
@Time: 2020/8/17 19:56
'''
from typing import List

"""
在一个二维矩阵中的左上角的格子开始走，每次只能向右或下走，目的是走到右下角的格子；
每个格子可能是正数、零、或负数，每走过一个格子，生命值相应减去（加上）此格子上的数值
初始生命值至少为多少，才可以走到右下角的格子（每一时刻的生命值都大于等于1）
"""

"""
设dp矩阵，dp[i][j]表示matrix[i][j]格子的位置走到终点至少需要多少生命值，那么目的就是求出dp[0][0]
设矩阵行数为m，列数为n，初始状态dp[m-1][n-1] = 1 if matrix[m-1][n-1] >= 0 else -matrix[m-1][n-1] + 1
然后以从右到左，从下到上的顺序推算dp[i][j]

如果向右走，
如果向下走，

dp可以设置为一维数组，因为它只和它下面和右面的格子有关
"""


def minHP(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 1
    m = len(matrix)
    n = len(matrix[0])
    if m >= n:
        rows, cols = m, n
    else:
        rows, cols = n, m
    dp = [0] * cols
    dp[-1] = 1 if matrix[rows - 1][cols - 1] >= 0 else -matrix[rows - 1][cols - 1] + 1
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if not (i == rows - 1 and j == cols - 1):
                right = 1 if j == cols - 1 else max(dp[j + 1] - matrix[i][j], 1)
                down = 1 if i == rows - 1 else max(dp[j] - matrix[i][j], 1)
                dp[j] = min(right, down)
    return dp[0]


print(minHP([[-2, -3, 3], [-5, -10, 1], [0, 30, -5]]))
