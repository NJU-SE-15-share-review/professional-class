# -*- coding:utf-8 -*-

# 创建一个ndarray数组对象，输入一组100以内的整数，数组shape为4*4，将数组中所有元素的总和、每行的平均值以及每列的平均值共9个数存入一个列表中，并返回该列表。
import numpy as np

class Solution():
    def solve(self, A):
        a1=0
        for i in range(4):
            for j in range(4):
                a1+=A[i][j]


        a2=0
        for i in range(4):
            a2+=A[0][i]

        a3=0
        for i in range(4):
            a3+=A[1][i]

        a4=0
        for i in range(4):
            a4+=A[2][i]

        a5=0
        for i in range(4):
            a5+=A[3][i]

        a6=0
        for i in range(4):
            a6+=A[i][0]

        a7=0
        for i in range(4):
            a7+=A[i][1]

        a8=0
        for i in range(4):
            a8+=A[i][2]

        a9=0
        for i in range(4):
            a9+=A[i][3]

        result=[a1,a2/4.0,a3*1.0/4.0,a4*1.0/4.0,a5/4.0,a6/4.0,a7/4.0,a8/4.0,a9/4.0]
        return result

if __name__ == '__main__':
    A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    S=Solution()
    print S.solve(A)