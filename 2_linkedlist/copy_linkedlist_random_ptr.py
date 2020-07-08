#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: copy_linkedlist_random_ptr.py
@Time: 2020/7/7 20:19
'''
import random

from mystruct.linkedlist import SinglyLinkedNode, _Node

"""
一个链表节点除了有一个指向下一节点的引用外，还有一个随机引用，指向链表中任一节点，复制此链表

进阶：
    时间O(n) 空间O(1)的解法
"""

"""
普通：使用哈希表的方法
将复制前的节点为key，复制后的节点为value存入一个字典d
再取出每一个节点连接它们的rand和next引用到相应节点
返回 d[head]
"""

"""
进阶：O(n) 无辅助空间
对每个节点，复制出副本节点，串在每个节点后面：
对于：1->2->3->4
把它变成：1->1'->2->2'->3->3'->4->4'
对每个副本节点，
    设置它的rand(它的rand就是原节点、也就是它前一个节点的rand的后一个)；
    然后将副本节点拆出来即可
"""

def copy_linkedlist_with_random_ptr(head: SinglyLinkedNode):
    if not head:
        return
    curr = head
    while curr:
        if curr.next:
            tmp = curr.next
            curr.next = SinglyLinkedNode(curr.val)
            curr.next.next = tmp
            curr = tmp
        else:
            curr.next = SinglyLinkedNode(curr.val)
    copy_head = head.next
    curr = head
    while curr:
        # 设置rand
        curr.next.rand = curr.rand.next if curr.rand else None
        curr = curr.next.next
    original, curr = head, copy_head
    # 拆分
    while curr:
        tmp = curr.next
        curr.next = curr.next.next
        original.next = tmp
    return copy_head

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self._l = []
        self._len = 0

    def add_to_tail(self, node: _Node):
        self.tail.next = node
        self.tail = node
        self._l.append(node)
        self._len += 1

    def __len__(self):
        return self._len

head = SinglyLinkedNode(random.randint(0, 20))
linked_list = LinkedList(head)
rand_idx = random.randint(0, len(linked_list))
if rand_idx == len(linked_list):
    head.rand = None
else:
    head.rand = head

curr = head
for _ in range(5):
    new = SinglyLinkedNode(random.randint(0, 20))
    rand_idx = random.randint(0, len(linked_list))
    if rand_idx == len(linked_list):
        new.rand = None
    else:
        new.rand = linked_list._l[rand_idx]
    curr.next = new

curr = head
while curr:
    print(curr.val, " ", curr.rand.val if curr.rand else None)
    curr = curr.next
copy_head = copy_linkedlist_with_random_ptr(head)

curr = copy_head
# while curr:
#     print(curr.val, " ", curr.rand.val if curr.rand else None)
#     curr = curr.next