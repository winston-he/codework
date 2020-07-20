#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: relocate.py
@Time: 2020/7/12 20:39
'''
from random import randint

from mystruct.linkedlist import SinglyLinkedNode

"""
按照左右半区的方式重新组合单链表
如果长度为偶数，则前N/2个节点为前半区，后N/2个节点为后半区；
如果长度为奇数，则前N/2个节点为前半区，后N/2+1个节点为后半区。
"""

# 快慢指针
# 奇数个，快指针next为None时，慢指针到了后半区头部
# 偶数个，快指针next.next为None时，慢指针到了后半区头部




def relocate(head: SinglyLinkedNode) -> SinglyLinkedNode:
    if not head or not head.next:
        return head
    fast = slow = head
    while fast.next:
        if not fast.next.next:
            slow = slow.next
            break
        slow = slow.next
        fast = fast.next.next
    first, second = head, slow
    curr = head
    while curr.next != slow:
        curr = curr.next
    curr.next = None
    while first:
        m, n = first.next, second.next
        first.next = second
        second.next = m
        first, second = m, n
        print(head.get_list())
    return head

curr = head = SinglyLinkedNode(1)

for i in range(8):
    curr.next = SinglyLinkedNode(i+2)
    curr = curr.next

print(head.get_list())

head = relocate(head)
print(head.get_list())