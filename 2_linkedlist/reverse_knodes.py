#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: reverse_knodes.py
@Time: 2020/7/8 20:11
'''
from mystruct.linkedlist import SinglyLinkedNode, generate_singly_linkedlist

"""
将一个单链表每K个节点逆序
如果用如下list代表一个链表，K=3：
    [1,2,3,4,5,6,7,8]
输出：
    [3,2,1,6,5,4,8,7]
第三组7, 8不足K(K=3)个，只逆序7,8即可
"""

def reverse_k_nodes(head: SinglyLinkedNode, k: int) -> SinglyLinkedNode:
    if k <= 1 or not head:
        return head
    start = end = head
    prev = None
    while start:
        curr, count = start, k
        while count > 1 and curr.next:
            curr = curr.next
        end = curr
        # prev要指向end
        if prev:
            prev.next = end
        # prev为None说明这是第一组
        else:
            head = end
        # start节点的next要指向end的next
        n, pre = start.next, start
        next_first = end.next
        while n != next_first:
            nxt = n.next
            n.next = pre
            pre = n
            n = nxt
        prev = start
    return head

h = generate_singly_linkedlist(8, 0, 10)
a = []
curr = h
while curr:
    a.append(curr.val)
    curr = curr.next

print(a)
h = reverse_k_nodes(h, 3)
curr = h
a = []
while curr:
    a.append(curr.val)
    curr = curr.next
