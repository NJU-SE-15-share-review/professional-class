# -*- coding:utf-8 -*-
# 独立双总体t检验通常用于检验两个相互独立的样本平均数与其各自所代表的总体平均数的差异是否显著。下面为t检验问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.ttest_ind(a,b,equal_var=True)对给定样本a与样本b进行t检验，其中equal_var为True时表明两样本所代表总体需要相同

from scipy import stats


def ttest():
    x = stats.norm.rvs(loc=5, scale=1, size=50)
    y = stats.norm.rvs(loc=2, scale=10, size=50)

    print (stats.ttest_ind(x, y))
    print (stats.ttest_ind(x, y, equal_var=False))


# the code should not be changed
if __name__ == '__main__':
    ttest()
