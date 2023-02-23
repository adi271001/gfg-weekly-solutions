import sys
from sys import stdin
input=stdin.readline
sys.setrecursionlimit(10**7)
from collections import  defaultdict
class Solution:
    def maxPower(self,n,edges):
        graph=[[] for _ in range(n)]
        for i in range(n-1):
            a,b=edges[i]
            graph[a].append(b)
            graph[b].append(a)
        sub={}
        sub1={}
        def dfs1(node,par):
            t=0
            t1=0
            for nie in graph[node]:
                if nie!=par:
                    dfs1(nie,node)
                    t+=sub1[nie]+nie
                    t1+=sub[nie]
            
            sub1[node]=t        
            sub[node]=t+t1
        dfs1(0,-1)
        res={}
        res[0]=sub[0]
        def dfs(node,par):
            if par!=-1:
                res[node]=(res[par]-sub[node]-sub1[node]-node)+((n-1)*(n))//2-sub1[node]-node+sub[node]
                sub[node]=res[node]
            for nie in graph[node]:
                if nie!=par:
                    dfs(nie,node)
        dfs(0,-1)
        t=[(res[el],el) for el in range(n)]
        t.sort(key=lambda x:(-x[0],x[1]))
        return t[0][1]
