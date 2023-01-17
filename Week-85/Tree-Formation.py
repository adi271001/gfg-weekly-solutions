Question Link: https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-85/problems/#
    
class Solution:
    def minimumCost(self, n, p):
        # code here
        v=[0]*(n+1)
        for l in range(1,n):
            v[l+1]+=1
            v[p[l]]+=1
        a=0
        for l in range(1,n+1):
            if (v[l]!=1):
                bn=v[l];
                a+=(bn*(bn+1))//2
                a-=1
        a+=1
        return a
