#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_length.py
@Time: 2020/7/16 21:46
'''
from typing import List

"""
给定一个无序整数数组，元素可以为负数，0，或正数。给定一个整数k，求数组中和为k的子数组的最大长度

补充问题1：给定一个无序整数数组，元素可以为负数，0，或正数。求正数和负数个数相等的最长子数组的长度
补充问题2：给定一个无序整数数组，求0和1个数相等的最长子数组的长度

时间O(N), 空间O(N)的解法
遍历一遍数组，设置一个字典为辅助空间
设置一个变量curr_sum, 当前位置的总和；一个变量maxlen，即所求的结果
字典的key表示当前位置i的数组的总和，即sum(arr[:i+1])，value表示出现这个值的最左位置
每遍历到一个元素(索引为i)，更新curr_sum, 并且看看字典中是否存在key: curr_sum-k，
如果存在，说明sum(arr[d[curr_sum-k : i+1]])的值为k，更新max_len: max_len = max(max_len, i-d[curr_sum-k]+1)
返回maxlen


关键点：字典应该有初始值key:0, value:-1, 因为如果满足条件的子数组是从arr[0]开始的，不加入此值就会出错。
比如：[1,2,3,3]
"""
def max_len(arr: List[int], k: int) -> int:
    maxlen = curr_sum = 0
    d = {0: -1}
    for i, v in enumerate(arr):
        curr_sum += v
        if curr_sum - k in d:
            maxlen = max(maxlen, i - d[curr_sum - k])
        if curr_sum not in d:
            d[curr_sum] = i
    return maxlen


"""
对于补充问题1，
如果数组中所有正数都转换为1，所有负数都转换为-1，那么问题就等同于把原始问题的参数k设置为0；所以先做转换，再调用函数max_len即可

补充问题2同理，把所有0转换为-1即可。
"""
