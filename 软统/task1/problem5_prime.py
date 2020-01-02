# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from __future__ import print_function
import math

class Solution():
    def solve(self, A):
        result = []
        for i in A:
            if self.prime(i):
                result.append(i)
        return result


    def prime(self, x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

print(Solution().solve())
