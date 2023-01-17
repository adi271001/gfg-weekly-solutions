Question Link: https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-85/problems/#
    
class Solution:
    def maximumPrefix(self, n, m, s, t):
        # code here
        k=0
        l=0
        p=1
        while(k<n and l<m):
            if (s[k]==t[l]):
                k+=1
                l+=1
                p+=1
            else:
                l+=1
        if (p==(n+1)):
            return -1
        return p
