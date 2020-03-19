# -*- coding: utf-8 -*-
# @Time : 2020/3/19 15:21
# @Author : wangmengmeng
"""请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy"""
class Solution:
    def replaceSpace(self, s):
        s= s.replace(' ','%20')
        print(s)

if __name__ == '__main__':
    s = 'We Are Happy'
    ss = Solution()
    ss.replaceSpace(s)
