# -*- coding:utf-8 -*-

# 完成函数solve，判断传入的整数列表A中的数字是否是素数，并将所有的素数保存到另一个列表中并返回。
import numpy as np

class Solution():
    def solve(self, A):
        # call function prime
        result=[]
        for i in A:
            if self.prime(i):
                result.append(i)
        return result




    # judge whether x is prime or not
    def prime(self, x):
        if x<=1:
            return False
        for i in range(2,int(np.sqrt(x))+1):
            if x%i==0:
                return False
        return True


if __name__ == '__main__':
    A = [23, 45, 76, 67, 17]
    S = Solution()
    print S.solve(A)