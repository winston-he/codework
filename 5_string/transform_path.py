#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: transform_path.py
@Time: 2020/8/26 20:12
'''

"""
最短转换路径
给定一个字符串列表，列表中每个字符串都不一样，给定一个字符串to，to一定存在于字符串列表中；
给定字符串start, 想要把start转变成to，每步只能转变一个字符，且每步得到的字符串必须存在于字符串列表中；
求所有的转换路径。

如：
arr = ['cab', 'acc', 'cbc', 'ccc', 'cac', 'cbb', 'aab', 'abb']
to = 'cab'

则所有转换路径：
abc -> abb -> aab -> cab
abc -> abb -> cbb -> cab
abc -> cbc -> cac -> cab
abc -> cbc -> cbb -> cab
"""