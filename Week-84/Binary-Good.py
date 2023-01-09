class Solution:
    def solve(self, S, N):
        a = [0]
        for i in S:
            if i=='0':
                if a[-1]!=0:
                    a.append(0)
            else:
                a[-1]+=1
        if a[-1]==0:
            a.pop()
        if len(a)==0:
            return 0
        a.sort()
        mid = len(a)//2
        x = a[mid]
        ans = 0
        for i in a:
            ans += abs(i-x)
        return ans
