#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: str2num.py
@Time: 2020/8/19 20:12
'''
from math import ceil

"""
将一个字符串转换为整型，注意，这里的整型用32位表示（尽管Python中的int类型并没有长度限制）

"""

"""
首先，判断一下这个字符串是否可以表示成数字：
    - 必须以“-”或数字开头
    - 如果以“0”开头，长度不能超过1
    - “-”后面必须全部为数字，且第一个数字不能为“0”
    
然后，开始转换
"""

def str_to_num(s: str) -> int:
    if len(s) == 0:
        return 0
    if s[0] == '0':
        return 0
    if s[0] == '-' or '0' < s[0] <= '9':
        for i in range(1, len(s)):
            if s[i] > '9' or s[i] < '0':
                return 0
    neg = s[0] == '-'

    min_int = -2**31
    res = 0
    min_remain = -(-min_int % 10)
    min_q = ceil(min_int / 10)
    if '0' < s[0] <= '9':
        res += ord('0') - ord(s[0])
    for c in s[1:]:
        if res < min_q or (res == min_q and ord('0') - ord(c) < min_remain):
            return 0
        res *= 10
        res += ord('0') - ord(c)
    if not neg and res == min_int:
        return 0
    return res if neg else -res

