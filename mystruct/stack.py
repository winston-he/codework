#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: stack.py
@Time: 2020/7/6 21:15
'''


class Stack:
    def __init__(self):
        self._s = []

    def push(self, val):
        self._s.append(val)

    def pop(self) -> int:
        if not self._s:
            raise ValueError("The stack is empty")
        return self._s.pop()

    def top(self):
        return None if not self._s else self._s[-1]

    def empty(self):
        return len(self._s) == 0
