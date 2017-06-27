#-*- coding:utf-8 -*-
# 下面为针对蒙提霍尔三门问题进行模拟中奖概率的代码，请仔细阅读，理解代码含义，并试着修改Monty Hall程序来模拟最原始的游戏规则。蒙提霍尔三门问题规则如下：
# （1）参赛者会看见三扇关闭的门，其中一扇的后面有一辆汽车，选中后面有车的那扇门就可以赢得该汽车，另两扇门后则各藏有一只山羊
# （2）当参赛者选定了一扇门，但未去开启它的时候，知道门后情形的节目主持人会开启剩下两扇门的其中一扇，露出其中一只山羊
# （3）主持人其后会问参赛者要不要换另一扇仍然关上的门

import random


def MontyHall(Dselect, Dchange):
    Dcar = random.randint(1, 3)
    # hit at the first and not change the mind
    if Dcar == Dselect and Dchange == 0:
        return 1
    # not hit at the first and not change the mind
    elif Dcar != Dselect and Dchange == 0:
        return 0
    # hit at the first and change the mind
    elif Dcar == Dselect and Dchange == 1:
        return 0
    # not hit at the first and change the mind
    else:
        return 1


if __name__ == '__main__':
    # repeat 10000 times
    n = 10000

    # not sure whether to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = random.randint(0, 1)
        win = win + MontyHall(Dselect, Dchange)
    print (float(win) / float(n))

    # be sure not to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = 0
        win = win + MontyHall(Dselect, Dchange)
    print (float(win) / float(n))

    # be sure to change the mind
    win = 0
    for i in range(n):
        Dselect = random.randint(1, 3)
        Dchange = 1
        win = win + MontyHall(Dselect, Dchange)
    print (float(win) / float(n))


