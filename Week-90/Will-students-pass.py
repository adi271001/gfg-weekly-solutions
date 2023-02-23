class Solution:
    def minimumCost(self, n, m, x, p, li):
        # code here
        ans=10**8
        for num in range(2**n):
            price=0
            tp=[0]*m
            for i in range(n):
                if (num&(1<<i)):
                    price+=p[i]
                    for j in range(m):
                        tp[j]+=li[i][j]
            y=0
            for i in range(m):
                if (tp[i]<x):
                    y=1
            if (y==0):
                ans=min(ans,price)
        if (ans==10**8):
            ans=-1
        return ans
