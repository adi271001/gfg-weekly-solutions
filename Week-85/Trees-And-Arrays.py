Question Link: https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-85/problems/#
    
class Solution:
    def maximumSum(self, n, k, p, a, b):
        # code here
        sp=-10**18
        dj=[[] for u in range(n+1)]
        for u in range(1,n):
            dj[p[u]].append(u+1)
        bp=[[sp]*(2*k) for u in range(n+1)]
        bp[1][k-1]=b[0]
        bp[1][k]=a[0]
        res=sp
        for u in range(1,n+1):
            for m in range(2*k):
                for y in dj[u]:
                    if (m):
                        bp[y][min(m-1,k-1)]=max(bp[y][min(m-1,k-1)],bp[u][m]+b[y-1])
                    if (m+1<2*k):
                        bp[y][max(m+1,k)]=max(bp[y][max(m+1,k)],bp[u][m]+a[y-1])
                if (len( dj[u])==0):
                    for m in range(2*k):
                        res=max(res,bp[u][m])
        return res
