#-*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from __future__ import print_function
# A group of researchers are interested in the possible effects of distracting stimuli during eating,
# such as an increase or decrease in the amount of food consumption.
# To test this hypothesis, they monitored food intake for a group of 44 patients who were randomised into two equal groups.
# The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions.
# Patients in the treatment group ate 52.1 grams of biscuits,
# with a standard deviation of 45.1 grams, and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams.
# Do these data provide convincing evidence that the average food intake is different for the patients in the treatment group?
# Assume the conditions for inference are satisfied.
#
# Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05
import math
from scipy.stats import t

class Solution():
	def solve(self):
		n1 = 22
		n2 = 22
		std2 = 45.1
		mean2 = 52.1
		std1 = 26.4
		mean1 = 27.1
		s_w_square = ((n1 - 1) * std1 * std1 + (n2 - 1) * std2 * std2) / (n1 + n2 - 2)
		stat_value = (mean1 - mean2) / (math.sqrt(s_w_square) * math.sqrt(1.0 / n1 + 1.0 / n2))
		t_value = t.isf(0.05, n1 + n2 - 2)
		return [min(n1 - 1, n2 - 1), -round(stat_value, 2), not stat_value <= -t_value]

print(Solution().solve())

