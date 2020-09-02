#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: robot_walk.py
@Time: 2020/7/27 20:52
'''
"""
机器人到达指定位置方法数：

设一个值N，代表机器人可以在1,2,3..,N, N个位置行走(N>=2)
设M，代表机器人的初始位置(1<=M<=N)
设K，代表机器人能走的步数
设P，代表机器人的目标位置

求机器人从M走到P有多少中走法
要求时间复杂度O(N*K)
"""


# 暴力递归法：
def enum_walk(N, M, K, P):
    def process(N, curr_pos, step_left, P, res):
        if step_left <= 0:
            if curr_pos == P:
                return res + 1
            else:
                return res
        if curr_pos > 1 and curr_pos < N:
            return process(N, curr_pos + 1, step_left - 1, P, res) + process(N, curr_pos - 1, step_left - 1, P, res)
        elif curr_pos == N:
            return process(N, curr_pos - 1, step_left - 1, P, res)
        else:
            return process(N, curr_pos + 1, step_left - 1, P, res)

    return process(N, M, K, P, 0)


"""
无后效性：一个递归状态的返回值与到达这个状态的路径无关  
N, M, K, P四个值，N(路径范围)，P(目标位置)是固定的；
M(当前位置) K(剩余步数)是变化的，
对M和K建立起一个动态规划矩阵dp，行对应M，列对应K；
由上面的暴力法可以看出：
(1) 当前位置为N时：
     dp[i][j] = dp[i-1][j-1]
(2) 当前位置为1时：
    dp[i][j] = dp[i+1][j-1]
(3) 当前位置在中间时：
    dp[i][j] = dp[i+1][j-1] + dp[i-1][j-1]
上面三种情况的转移方程都只依赖于上一行的值，使用一个长度为M的初始值的数组表示dp即可
最终dp[M-1][K-1] 就是答案

初始状态，当步数为0时，dp[i][0]除了目标位置为1以外，其他位置都是0
空间复杂度O(K), 时间复杂度O(MK)

"""


# 动态规划解法
def dp_walk(N, M, K, P):
    pass


print("暴力递归法：一共有{}种走法".format(enum_walk(7, 4, 9, 5)))
