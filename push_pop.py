# -*- coding: utf-8 -*-
# @Time : 2020/3/19 21:33
# @Author : wangmengmeng
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
