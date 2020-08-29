#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: new_char.py
@Time: 2020/8/29 13:11
'''

"""
找到指定的新类型字符

新类型字符定义为：
     - 1. 长度为1或2
     - 2. 由一个小写字母构成
     - 3. 由一个大写字母+一个小写字母构成
     - 4. 由两个大写字母构成
给定一个位置k，求k位置上的新类型字符
"""

"""
从k-1位置开始，向左统计连续的大写字母个数，
- 如果为奇数个，那么第k个字符必须和第k-1个字符组成一个新型字符；
- 如果是偶数个，
    - 如果第k个字符是大写的，那么它只能和下一个字符（k+1）组成一个新型字符；
    - 如果第k个字符是小写的，那么它自己就是一个新型字符
（假定给定字符串是合法的）
"""


def get_new_char(s: str, k: int) -> str:
    count, pos = 0, k-1
    while pos >= 0 and 'A' <= s[pos] <= 'Z':
        pos -= 1
        count += 1
    if count % 2 == 1:
        return s[k-1] + s[k]
    else:
        if 'A' <= s[k] <= 'Z':
            return s[k] + s[k+1]
        else:
            return s[k]
