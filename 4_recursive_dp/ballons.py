#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: ballons.py
@Time: 2020/8/3 20:18
'''

"""
给定一个整数数组，表示一排气球
如果打爆一个气球，它的分数是X，那么：
    - 如果打爆的气球左右都有没打爆的气球，找到它左边最近的气球，记分数为L；找到它右边最近的气球，记分数为R；此时得分为L*X*R
    - 如果仅左边有没打爆的气球，找到它左边最近的气球，记分数为L，此时得分为L*X；
    - 如果仅右边有没打爆的气球，找到它右边最近的气球，记分数为R，此时得分为R*X；
    - 如果左右都全打爆了，此时得分为X
求能得到的最大分数
"""

"""
暴力法：
假设数组记为B(ballons)，设左边界为L，右边界为R，要求打爆L到R范围内的气球获得的最大分数：
    - 如果最后打爆B[L], 则得到的分数应为B[L]*B[L-1]*B[R+1] + process(L+1, R)
    - 如果最后打爆B[R], 则得到的分数应为B[R]*B[L-1]*B[R+1] + process(L, R-1)
    - 如果最后打爆B[i](L<i<R), 则得到的分数应为process(L, i-1) + process(i+1, R) + B[i]*B[L-1]*B[R+1]
打爆L到R范围内的气球获得的最大分数就是上面三种情况的最大值
"""


def process(B, L, R):
    # 只有一个气球
    if L == R:
        return B[L - 1] * B[L] * B[R + 1]
    left_as_last = B[L] * B[L - 1] * B[R + 1] + process(B, L + 1, R)
    right_as_last = B[R] * B[L - 1] * B[R + 1] + process(B, L, R - 1)
    max_val = max(left_as_last, right_as_last)
    for i in range(L + 1, R):
        middle_as_last = process(B, L, i - 1) + process(B, i + 1, R) + B[i] * B[L - 1] * B[R + 1]
        max_val = max(max_val, middle_as_last)
    return max_val


# 暴力
def ballon_score_enum(B):
    if not B:
        return 0
    if len(B) == 1:
        return B[0]
    # 左右补1，可以使得代码中不需进行越界判断
    C = [1] * (len(B) + 2)
    for i in range(1, len(B)+1):
        C[i] = B[i-1]
    return process(C, 1, len(B))


print(ballon_score_enum([3, 2, 5]))
