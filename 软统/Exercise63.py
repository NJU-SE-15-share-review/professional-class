# -*- coding:utf-8 -*-

# 已知列表fruits中顺序保存了某商店每日出售的水果品名，例如fruits=['apple','banana','cherry','pineapple','banana','peach','pear','peach','cherry' ]
# ，完成函数solve()计算每一种水果的出售次数，存入字典result中并将结果返回

class Solution():
    def solve(self, a):
        b=list(set(a))
        b.sort(key=a.index)

        result={}
        for i in b:
            result[i]=0

        for i in a:
            value=result[i]
            result[i]=value+1
        return result









if __name__ == '__main__':
    A=['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]
    S=Solution()
    print S.solve(A)