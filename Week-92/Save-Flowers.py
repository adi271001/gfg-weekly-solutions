import sys
sys.setrecursionlimit(100000)

class Solution:
    def saveFlowers(self, n, arr, s):
        dp=[[-1]*(n+1) for i in range(2)]
        def my(have,ind):
            if ind == 0:
                return 0 if (have or s[ind] == '0') else arr[ind]
            if dp[have][ind] != -1:
                return dp[have][ind]
            ans = 0
            if s[ind] == '1':
                if have:
                    ans = arr[ind-1] + my(1,ind-1)
                else:
                    ans = max(arr[ind] + my(0,ind-1), arr[ind-1] + my(1,ind-1))
            else:
                ans = my(0,ind-1)
            dp[have][ind] = ans
            return ans
        return my(0,n-1)
