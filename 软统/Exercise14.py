# -*- coding:utf-8 -*-

# 下面模拟了分别服从参数1.5、1.0、0.5的指数分布随机变量rv1、rv2、rv3。并在[0,20]平均间隔地取100个值作为随机值。在上述基础上，利用随机值作为x轴，相应概率值作为y轴，画出其直方图，可大概体现指数分布的概率密度图的特征。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如参数为5.0，怎么修改代码中expon函数的参数呢？
# （3）设想一种可使用指数分布计算概率的情景，并用代码实现吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.expon(scale)函数返回符合指数分布的参数为scale的随机变量rv，经常配合使用rv.pdf(x)计算其概率密度值，参数x为序列
# （3）numpy.linspace(start,stop,num)返回[start,stop)之间的均匀间隔的num个数字组成的序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E

def expon_pdf():
	x = np.linspace(0, 20, 100)#return evenly spaced samples, calculated over the interval [0,20]
	rv1=E(scale = 1.5)#the scale is 1.5
	rv2=E(scale = 1.0)#the scale is 1.0
	rv3=E(scale = 0.5)#the scale is 0.5

	plt.plot(x, rv1.pdf(x), color='green')#make chart
	plt.plot(x, rv2.pdf(x), color='blue')#make chart
	plt.plot(x, rv3.pdf(x), color='red')#make chart
	plt.savefig('fig.png')

#the code should not be changed
if __name__ == '__main__':
    expon_pdf()