# -*- coding: utf-8 -*-
# @Time : 2020/3/19 17:31
# @Author : wangmengmeng
"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        l = list()
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]

