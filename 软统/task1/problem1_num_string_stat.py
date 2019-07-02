# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from __future__ import print_function
# 已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果
from collections import defaultdict


class Solution():
    def solve(self, A):
        number_dict = {}
        for i in range(10):
            number_dict[i] = 0
        for s in A:
            for c in s:
                number_dict[int(c)] += 1
        return number_dict

A = ['12','34','567', '36','809','120']
print(Solution().solve(A))
