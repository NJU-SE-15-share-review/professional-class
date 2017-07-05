# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
# Is there strong evidence of global warming?
# Let's consider a small scale example, ' \
#    'comparing how temperatures have changed is the US from 1968 to 2008. ' \
#    'The daily high temperature reading on January 1 was collected in 1968 and 2008 ' \
#    'for 51 randomly selected locations in the continental US. ' \
#    'Then the difference between the two readings (temperature in 2008 - temperature in 1968) ' \
#    'was calculated for each of the 51 values was 1.1 degree with a standard deviation of 4.9 degrees. ' \
#    'We are interested in determining whether these data provide strong evidence of temperature warming in the continental US.
from scipy.stats import t
import math

class Solution():
    def solve(self):
        n = 51
        std = 4.9
        mean = 1.1
        t_value = t.isf(0.025, n - 1)
        stat_value = mean / (std / math.sqrt(n))
        return [round(n - 1, 2), round(stat_value, 2), not stat_value <= -t_value]

print Solution().solve()
