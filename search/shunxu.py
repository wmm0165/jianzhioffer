# -*- coding: utf-8 -*-
# @Time : 2020/3/19 22:36
# @Author : wangmengmeng
def search(list, k):
    for i in range(len(list)):
        if list[i] == k:
            return i
    return 0
