# -*- coding:utf-8 -*-

# Wilcoxon秩和检验通常用于检验成对观测数据之差是否来自均值为0的总体。下面为Wilcoxon秩和检验问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.chisquare(x,y)对给定样本x及y进行秩和检验

from scipy import stats


def chisquare():
    A=[16, 18, 16, 14, 12, 12]
    B=[16, 16, 16, 16, 16, 8]

    print (stats.chisquare(A,B))


#the code should not be changed
if __name__ == '__main__':
    chisquare()