# -*- coding:utf-8 -*-

# 下面为大数定律二，辛钦大数定律的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）试利用其他独立同分布的随机变量验证辛钦大数定律。

# （1）此题为普通编程练习题
# （2）scipy.stats.binom.rvs(n,p,size=1)函数返回size个符合二项分布的随机变量,其独立试验次数为n，每次成功的概率为
# （3）scipy.stats.poisson.rvs(mu,size=1)函数返回size个符合泊松分布的随机变量,其单位时间内随机事件的平均发生率为mu
# （4）scipy.stats.norm.rvs(loc=0,scale=1,size=1)函数返回size个符合正态分布的随机变量，其数学期望为loc，标准差为scale

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm

def law_of_large_numbers():
	x = np.arange(1, 1001, 1)
	r1 = binom.rvs(10, 0.6, size=1000)
	r2 = poisson.rvs(mu=6, size=1000)
	r3 = norm.rvs(loc=6, size=1000)

	y = []
	rsum=0.0
	for i in range(1000):
		rsum=rsum+(r1[i]+r2[i]+r3[i])
		y.append(rsum/((i+1)*3)-6)

	plt.plot(x, y, color='red')
	plt.savefig('law_of_large_numbers.png')

#the code should not be changed
if __name__ == '__main__':
	law_of_large_numbers()