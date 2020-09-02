#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: min_len_includes_substr.py
@Time: 2020/8/29 13:36
'''
from collections import defaultdict

"""
给定两个字符串s1, s2, 
求s1的子串中包含s2所有字符的最小子串长度
s1 = "abcde" s2 = "ac"
s1的子串中，"abc"包含了s2中所有字符，它是最短的包含s2所有字符的s1子串，因此返回3
"""

"""
需要一个哈希表存储s2中字符的数量
基本思路就是设定左右边界left和right，
    - right不断向右扩张使得哈希表中的剩余字符数量不断被减少；
    - 当满足条件之后（s2中所有字符都被包含在子串中），right停止移动，left开始移动
    - left移动的目的就是排除一些无用的字符，当left移动到的位置排除了一个必须的字符时，left停止移动；
    -重复上述步骤，并在每次条件满足时更新最小长度
"""


def min_length(s1: str, s2: str) -> int:
    if not s2 or not s1 or len(s1) < len(s2):
        return 0
    # 统计s2的字符个数
    d = defaultdict(int)
    for c in s2:
        d[c] += 1
    # match是剩余的需要满足的字符数量
    right = left = 0
    match = len(s2)
    res = float("inf")
    while right < len(s1):
        while right < len(s1) and match > 0:
            if d[s1[right]] > 0:
                match -= 1
            d[s1[right]] -= 1
            right += 1
        while right < len(s1) and left < len(s1) and match == 0:
            # 如果小于0，意味着如果排除了这个字符也仍然满足条件
            if d[s1[left]] >= 0:
                match += 1
            d[s1[left]] += 1
            left += 1
        res = min(res, right - left)
    return res if res < float("inf") else 0


print(min_length('adabbca', 'acb'))