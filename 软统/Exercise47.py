# -*- coding:utf-8 -*-

# Does being part of a support group affect the ability of people to quit smoking? A country health department enrolled 300 smokers in a randomized experiment. 150 participants were assigned to a group that used a nicotine patch and met weekly with a support group; the other 150 received the patch and did not meet with a support group. At the end of the study, 40 of the participants in the patch plus support group had quit smoking while only 30 smokers had quit in the other group.
#  (1) Create a two-way table presenting the results of this study.
#  (2) Answer each of the following questions under the null hypothesis that being part of a support group does not affect the ability of people to quit smoking, and indicate whether the expected values are higher or lower than the observed values.
#       * How many subjects in the "patch+support" group would you expect to quit?  coding this part
#       * How many subjects in the "patch only" group would you expect to not quit?

#(1)with a support group?   Yes     No      Total
#       Quit                40      30      70
#       Not Quit            110     120     230
#       Total               150     150     300


from __future__ import print_function
class Solution():
    def solve(self):
        return 70*150/300

print(Solution().solve())