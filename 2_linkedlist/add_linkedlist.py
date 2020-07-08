#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: add_linkedlist.py
@Time: 2020/7/8 19:30
'''

"""
将两个代表数字的链表相加并返回结果：
输入:
    h1: 9->3->7 h2: 6->3
输出：
    1->0->0->0
即937 + 63 = 1000 

可以利用栈结构，也可以对链表逆序，取决于是否允许修改链表
"""

from mystruct.linkedlist import SinglyLinkedNode, generate_singly_linkedlist


# 对链表逆序求解
def reverse_linkedlist(head: SinglyLinkedNode):
    if not head:
        return
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def add_linkedlist(h1: SinglyLinkedNode, h2: SinglyLinkedNode):
    h1 = reverse_linkedlist(h1)
    h2 = reverse_linkedlist(h2)

    curr_1, curr_2 = h1, h2
    carry = 0
    while curr_1 and curr_2:
        curr_sum = curr_1.val + curr_2.val + carry
        if curr_sum > 9:
            curr_sum %= 10
            carry = 1
        else:
            carry = 0
        curr_1.val = curr_sum
        curr_1, curr_2 = curr_1.next, curr_2.next
    while curr_1:
        curr_sum = curr_1.val + carry
        if curr_sum > 9:
            curr_sum %= 10
            carry = 1
        else:
            carry = 0
        curr_1.val = curr_sum
        curr_1 = curr_1.next
    c = curr_2
    while curr_2:
        curr_sum = curr_2.val + carry
        if curr_sum > 9:
            curr_sum %= 10
            carry = 1
        else:
            carry = 0
        curr_2.val = curr_sum
        curr_2 = curr_2.next
    curr = h1
    while curr.next:
        curr = curr.next
    curr.next = c
    if carry:
        h = SinglyLinkedNode(1)
        h.next = reverse_linkedlist(h1)
    else:
        h = reverse_linkedlist(h1)
    return h

h1 = generate_singly_linkedlist(10, 0, 9)
h2 = generate_singly_linkedlist(3, 0, 9)

c1, c2 = h1, h2
a, b = '', ''
while c1:
    a += str(c1.val)
    c1 = c1.next
while c2:
    b += str(c2.val)
    c2 = c2.next


print(int(a) + int(b))


h = add_linkedlist(h1, h2)
while h:
    print(h.val)
    h = h.next

