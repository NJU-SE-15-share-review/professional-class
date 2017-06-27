# -*- coding:utf-8 -*-

# 单总体t检验通常用于检验一个样本平均数与一个已知的总体平均数的差异是否显著。下面为t检验问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.ttest_1sample(a,popmean)对给定样本a与总体平均值进行t检验

from scipy import stats

def ttest():
	x = stats.norm.rvs(loc=5, scale=10, size=50)

	print (stats.ttest_1samp(x,5.0))
	print (stats.ttest_1samp(x,1.0))

#the code should not be changed
if __name__ == '__main__':
	ttest()