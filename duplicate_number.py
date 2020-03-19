# -*- coding: utf-8 -*-
# @Time : 2020/3/19 16:42
# @Author : wangmengmeng
"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""

from collections import Counter


# class Solution:
#     def duplicate(self, numbers, duplication):
#         pass


def duplicate(numbers,duplication):
    duplication = []
    dict_data = Counter(numbers)
    num = [key for key, value in dict_data.items() if value > 1][0]
    duplication.append(num)
    print(duplication)
    if duplication is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    numbers = [2,1,3,1,4]
    duplicate(numbers,duplication = [])
