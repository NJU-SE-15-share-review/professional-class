# -*- coding:utf-8 -*-

# 下面为连续指数分布的数字特征示例，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
#
# （1）此题为普通编程练习题
# （2）lambda argument_list:expression用来表示匿名函数
# （3）numpy.exp(x)计算x的指数
# （4）numpy.inf表示正无穷大
# （5）scipy.integrate.quad(func,a,b)计算func函数从a至b的积分
# （6）scipy.stats.expon(scale)函数返回符合指数分布的参数为scale的随机变量rv
# （7）rv.moment(n,*args,*kwds)返回随机变量的n阶距


import numpy as np
from scipy import integrate
from scipy.stats import expon


def nc_of_expon():
    # 1st non-center moment of expon distribution whose lambda is 0.5
    E1 = lambda x: x * 0.5 * np.exp(-x / 2)
    # 2nd non-center moment of expon distribution whose lambda is 0.5
    E2 = lambda x: x ** 2 * 0.5 * np.exp(-x / 2)
    print(integrate.quad(E1, 0, np.inf))
    print(integrate.quad(E2, 0, np.inf))

    print(expon(scale=2).moment(1))
    print(expon(scale=2).moment(2))


# the code should not be changed
if __name__ == '__main__':
    nc_of_expon()
