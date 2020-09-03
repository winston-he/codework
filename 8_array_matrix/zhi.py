#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: zhi.py
@Time: 2020/9/3 19:46
'''
from typing import List

"""
之字形打印矩阵
"""

def print_matrix_zig_zag(matrix: List[List[int]]):
    if not matrix:
        return
    count = len(matrix) * len(matrix[0]) # 打印了的元素的个数
    h = [0, 0]
    v = [0, 0]
    up_down = False
    while count != 0:
        num = abs(h[0]-v[0]) + 1
        count -= num
        x, y = h if up_down else v
        for i in range(num):
            print(matrix[x][y])
            if up_down:
                x += 1
                y -= 1
            else:
                x -= 1
                y += 1
        if h[1] == len(matrix[0])-1:
            h[0] += 1
        else:
            h[1] += 1
        if v[0] == len(matrix)-1:
            v[1] += 1
        else:
            v[0] += 1
        up_down = not up_down

