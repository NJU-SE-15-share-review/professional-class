#-*- coding:utf-8 -*-
from __future__ import print_function
import random


#this function may spend a little time to execute
def MontyCarlo():
    n = 1000000
    k = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            k = k + 1
    return 4 * float(k) / float(n)

if __name__ == '__main__':
    pi = MontyCarlo()
    #print out the result
    print(pi)