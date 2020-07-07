#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: monotonous_stack.py
@Time: 2020/7/6 21:03
'''
from typing import List

from mystruct.stack import Stack


def get_near_less_no_repeat(arr: List[int]):
    s = Stack()
    res = [None for _ in range(len(arr))]
    for i, n in enumerate(arr):
        while not s.empty() and n < arr[s.top()]:
            curr = s.pop()
            res[curr] = (-1 if s.empty() else s.top(), i)
        s.push(i)
    while not s.empty():
        curr = s.pop()
        res[curr] = (-1 if s.empty() else s.top(), -1)
    return res


if __name__ == '__main__':
    a = [3, 4, 1, 5, 6, 2, 7]
    print(get_near_less_no_repeat(a))