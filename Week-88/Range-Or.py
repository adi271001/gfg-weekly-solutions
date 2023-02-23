class Solution:
    def rangeOR(self,n):
        # code here
        res = 0
        k = 1
        while k <= n:
            res |= k
            k = k << 1
        return res
