class Solution:
    def solve(self, s, K): 
        #code here
        n = len(s)
        vis = [False]*n
        q = []
        ans = 0
        for i in range(n):
            if s[i] == '1':
                q.append([i, 0])
                vis[i] = True
                ans+=1
        firstIdx = 0
        while len(q)>firstIdx:
            f = q[firstIdx];
            firstIdx+=1
            if f[1] < K:
                if f[0] - 1 >= 0:
                    if vis[f[0] - 1] == False:
                        q.append([f[0] - 1, f[1] + 1])
                        vis[f[0] - 1] = True
                        ans+=1
                if f[0] + 1 < n:
                    if vis[f[0] + 1] == False:
                        q.append([f[0] + 1, f[1] + 1])
                        vis[f[0] + 1] = True
                        ans+=1
        return ans
