# -*- coding:utf-8 -*-

# 在Numpy中，多项式函数的系数可以用一维数组表示，例如对于f(x)=2x^3-x+1可表示为f=np.array([2.0,0.0,-1.0,1.0])，
# 而np.poly1d()方法可以将多项式转换为poly1d(一元多项式)对象，返回多项式函数的值，请利用poly1d()方法计算多项式g(x)(例如g(x)=x^2+2x+1)和f(x)的乘积并将结果返回。

import numpy as np


class Solution():
    def solve(self, A):
        fx=np.array([2.0,0.0,-1.0,1.0])
        gx=A
        maxe=len(fx)+len(gx)-2
        resultx=[0 for i in range(maxe+1)]
        print resultx
        for i in range(len(fx)):
            for j in range(len(gx)):
                resultx[i+j]+=fx[i]*gx[j]

        return np.poly1d(resultx)


if __name__ == '__main__':
    A = np.array([1,2,1])
    S = Solution()
    print S.solve(A)

