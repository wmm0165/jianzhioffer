# -*- coding: utf-8 -*-
# @Time : 2020/3/19 17:42
# @Author : wangmengmeng
from collections import Counter

def FindNumsAppearOnce(array):
    dict_data = Counter(array)
    once = [key for key,value in dict_data.items() if value == 1]
    print(once)
    return once


if __name__ == '__main__':
    array = [2,2,3,4]
    FindNumsAppearOnce(array)