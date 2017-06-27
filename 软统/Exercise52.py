# -*- coding:utf-8 -*-

# 卡方拟合优度检验通常用于根据样本的频数分布来推断总体的分布。下面为卡方拟合优度检验问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.chisquare(f_obs,f_exp=None)对给定样本f-obs及其期望分布f_exp进行检验，其中f_exp为None时认为期望分布为均匀分

from scipy import stats

def chisquare():
    A=[16, 18, 16, 14, 12, 12]
    B=[16, 16, 16, 16, 16, 8]

    print (stats.chisquare(A))
    print (stats.chisquare(A, f_exp=B))

#the code should not be changed
if __name__ == '__main__':
    chisquare()