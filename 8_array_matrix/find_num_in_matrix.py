#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: find_num_in_matrix.py
@Time: 2020/9/5 15:17
'''
from typing import List, Tuple

"""
在二维数组中找到指定的数,

以左下角为起点，如果当前数比目标数大，就往上走，否则往右走，直至当前数等于目标数，返回坐标
或以右上角为起点也可
"""


def find_num(matrix: List[List[int]], target: int) -> Tuple[int, int]:
    if not matrix or not matrix[0]:
        return
    row, col = len(matrix) - 1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] > target:
            row -= 1
        else:
            col += 1
