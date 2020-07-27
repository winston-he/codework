#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: max_happy.py
@Time: 2020/7/26 12:51
'''

"""
P169 派对的最大快乐值

每个员工有一个快乐值，一个直接上司，和若干直接下属
现开始一个派对：
    - 如果某个员工参加，则他的直接下属都不能参加
    - 派对的整体快乐值是所有参加人员的累加值
    - 求最大快乐值
使时间复杂度为O(N)
"""


class Employee:
    def __init__(self, happy: int):
        self.happy = happy
        self.subordinates = []


def max_happy(boss: Employee) -> tuple:
    yes, no = boss.happy, 0
    if len(boss.subordinates) == 0:
        return yes, no
    for sub in boss.subordinates:
        sub_yes, sub_no = max_happy(sub)
        yes += sub_no
        no += max(sub_yes, sub_no)
    return yes, no