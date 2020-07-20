#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: linkedlist.py
@Time: 2020/7/7 19:28
'''
import random


class _Node:
    pass


class SinglyLinkedNode(_Node):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_list(self):
        l = []
        curr = self
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l
    def __str__(self):
        return str(self.val)

class DoublyLinkedNode(_Node):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def generate_singly_linkedlist(length, a, b):
    h = SinglyLinkedNode(random.randint(a, b))
    curr = h
    for _ in range(length-1):
        curr.next = SinglyLinkedNode(random.randint(a, b))
        curr = curr.next
    return h