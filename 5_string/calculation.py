#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: calculation.py
@Time: 2020/8/27 20:01
'''
"""
一个字符串包含了数字、加减乘除符号、以及左右括号，它表示了一个四则运算的式子，要求计算它的结果
"""

"""
1. 总体上，用一个双端队列保存算式
2. 遇到左括号，进入递归过程，遇到右括号，结束递归过程，并返回当前结果以及遍历的位置
"""