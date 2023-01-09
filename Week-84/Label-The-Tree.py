def Util(self, cur, adj):
        if len(adj[cur]) == 0:
            a=[]
            a.append(cur)
            return a
        a = [] 
        temp = []
        for i in adj[cur]:
            temp = self.Util(i, adj)
            for j in temp:
                a.append(j)
        sz = len(a)
        sz //= 2
        a.insert(sz, cur)
        return a
        
    def labelTree(self, N, p):
        adj = [[] for i in range(N)]
        for i in range(1,N):
            adj[p[i]].append(i)
        temp = self.Util(0, adj)
        res = [0]*(N)
        for i in range(N):
            res[temp[i]] = i + 1
        return res
