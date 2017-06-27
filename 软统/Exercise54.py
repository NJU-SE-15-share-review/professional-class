# -*- coding:utf-8 -*-

# KS检验通常用于检验单一样本是否服从某特定分布，或者两样本是否来自相同分布。下面为KS检验问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.ks_2samp(data1,data2)对给定样本data1及data2进行KS双边检验

from scipy import stats


def kstest():
    n1=200
    n2=300
    a = stats.norm.rvs(size=n1, loc=0, scale=1)
    b = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
    c = stats.norm.rvs(size=n2, loc=0.01, scale=1)

    print (stats.ks_2samp(a, b))
    print (stats.ks_2samp(a, c))

#the code should not be changed
if __name__ == '__main__':
    kstest()