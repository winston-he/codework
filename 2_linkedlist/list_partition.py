#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: list_partition.py
@Time: 2020/7/7 19:27
'''
import random

from mystruct.linkedlist import SinglyLinkedNode

"""
输入一个单链表：9->0->4->5->1和一个pivot: 3, 调整链表的顺序，使得链表左半部的元素小于3，中间的元素等于3，右半部的元素大于三，
左中右三个部分的内部顺序可忽略

进阶：
    1. 保持三个部分元素原先的相对顺序
    2. 时间复杂度达到O(n), 空间复杂度达到O(1)
"""

"""
普通：
遍历链表，将元素存储到数组中，在数组中使用快排中的分区方法进行分区，再把数组输出到链表上
"""
def list_partition_amateur(listhead: SinglyLinkedNode, pivot: int):
    arr = []
    curr = listhead
    while curr:
        arr.append(curr)
        curr = curr.next
    small, end, index = -1, len(arr)-1, 0
    while index != end:
        if arr[index].val > pivot:
            arr[index], arr[end] = arr[end], arr[index]
            end -= 1
        elif arr[index].val < pivot:
            small += 1
            arr[small], arr[index] = arr[index], arr[small]
            index += 1
        else:
            index += 1
    head = curr = arr[0]
    for n in arr[1:]:
        curr.next = n
        curr = curr.next
    return head

"""
将链表拆成small, equal, big三个部分，再重新组合
"""
def list_partition_advanced(listhead: SinglyLinkedNode):
    pass

if __name__ == '__main__':
    curr = head = SinglyLinkedNode(random.randint(0, 20))
    for _ in range(5):
        curr.next = SinglyLinkedNode(random.randint(0, 20))
        curr = curr.next
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    head = list_partition_amateur(head, 5)
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next