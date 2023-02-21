class Solution:
    def dfs(self, A, i, par, D):
        if len(A[i])==1 and A[i][0]==par:
            return 0
        mini = float('inf')
        for child in A[i]:
            if (child != par):
                op1 = self.dfs(A, child, i, D)
                mini = min(mini, op1)
        D[i] = 1 + mini
        return D[i]
    
    def dfs1(self, A, i, par, curr, d, D, ini):
        if len(A[i])==1 and A[i][0]==par:
            return d
        ans = 0
        if (curr==0):
            d += D[i]
            curr = ini
        for child in A[i]:
            if (child != par):
                op1 = self.dfs1(A, child, i, curr-1, d+1, D, ini)
                ans = max(ans, op1)
        return ans

    def solve(self, n, k, par):
        A = [[] for i in range (n+1)]
        for i in range (1, len(par)):
            a = par[i]
            b = i+1
            A[a].append(b)
            A[b].append(a)
        
        D = [0]*(n+1)
        self.dfs(A, 1, -1, D)
        return self.dfs1(A, 1, -1, k, 0, D, k)
