# -*- coding:utf-8 -*-

# 为正态分布的数字特征示例，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）lambda argument_list:expression用来表示匿名函数
# （3）scipy.stats.norm.expect(func,loc=0,scale=1)函数返回func函数相对于正态分布的期望值，其中函数f(x)相对于分布dist的期望值定义为E[x]=Integral(f(x) * dist.pdf(x))

from scipy.stats import norm


def nc_of_norm():
    f1 = lambda x: x ** 4
    f2 = lambda x: x ** 2 - x + 2

    print(norm.expect(f1, loc=1, scale=2))
    print(norm.expect(f2, loc=2, scale=5))


# the code should not be changed
if __name__ == '__main__':
    nc_of_norm()
