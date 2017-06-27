# -*- coding:utf-8 -*-

# 已知有一个由数字字符串构成的列表，统计列表中数字字符'0'-'9'各自出现的次数并返回统计结果


class Solution():
    def solve(self, a):
        result={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for i in a:
            for j in i:
                result[int(j)]+=1

        return result



if __name__ == '__main__':
    a=['12','34','567', '36','809','120']
    S=Solution()
    print S.solve(a)


