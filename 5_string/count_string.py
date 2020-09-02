#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: count_string.py
@Time: 2020/8/20 20:41
'''

"""
字符串的统计字符串
1. 给定一个字符串，返回它的统计字符串
如，给定aabbccc, 返回a_2_b_2_c_3

2. 给定一个统计字符串及一个索引index，返回原字符串的第index个字符
如，给定a_2_b_2_c_3和4，返回4，因为aabbccc索引为4的字符是c
"""


def get_count_string(s: str) -> str:
    if s == '':
        return s
    res = s[0] + '_'
    count, curr = 0, s[0]
    for i in range(len(s)):
        if s[i] == curr:
            count += 1
        else:
            curr = s[i]
            res += str(count) + '_' + s[i] + '_'
            count = 1
    # 最后一个字符
    res += str(count)
    return res


def get_chr_from_count_string(s: str, index: int) -> str:
    target, flag, pos = s[0], False, 0
    for i in range(2, len(s), 4):
        pos += int(s[i])
        if index <= pos-1:
            break
    return s[i-2]