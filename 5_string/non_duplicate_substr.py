#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: non_duplicate_substr.py
@Time: 2020/8/27 20:34
'''
"""
最长无重复子串的长度
"""

"""
a a b c b
使用一个哈希表
key 代表一个字符，value代表这个字符最后出现的位置

一个变量start，表示当前不重复子串的开始位置
"""
from collections import defaultdict


def max_non_duplicate_substring(s: str) -> int:
    if not s:
        return 0
    start, res, curr = 0, 1, 1
    d = dict()
    d[s[0]] = 0
    for i, c in enumerate(s):
        if i == 0:
            continue
        if c in d:
            # 这个字符在当前子串中
            if d[c] >= start:
                start = d[c] + 1
                res = max(res, curr)
                curr = i - d[c]
            else:
                curr += 1
        else:
            curr += 1
        d[c] = i
    return max(res, curr)

print(max_non_duplicate_substring("dvdf"))