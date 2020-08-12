# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from __future__ import print_function
# 已知列表fruits中顺序保存了某商店每日出售的水果品名,
# 例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry' ]，
# 完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回

class Solution():
    def solve(self, A):
        result = {}
        for s in A:
            if s in result:
                result[s] += 1
            else:
                result[s] = 1
        return result

A = ['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]
print(Solution().solve(A))
