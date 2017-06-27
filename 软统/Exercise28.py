# -*- coding:utf-8 -*-

# 下面为大数定律一，伯努利大数定律的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）调整泊松分布的参数，看看结果会如何变化？

# （1）此题为普通编程练习题
# （2）scipy.stats.bernoulli.rvs(p,loc=0,size=1)返回size个符合泊松分布的随机变量

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def law_of_large_numbers():
	x = np.arange(1, 1001, 1) 
	r = bernoulli.rvs(0.3, size=1000)
	y = []
	rsum =0.0
	for i in range(1000):
		if r[i]==1:
			rsum=rsum+1
		y.append(rsum/(i+1))
	plt.plot(x, y, color='red')
	plt.savefig('law_of_large_numbers.png')

#the code should not be changed
if __name__ == '__main__':
	law_of_large_numbers()