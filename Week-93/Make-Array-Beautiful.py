class Solution:
    def minimumOperations(self, n, a):
        ct1 = ct2 = 0
        for i in range(n):
            if a[i] % 3 == 1:
                ct1 += 1
            elif a[i] % 3 == 2:
                ct2 += 1
        if ct1 == ct2:
            return ct1
        elif ct1 > ct2:
            ans = ct2
            ct1 -= ct2
            if ct1 % 3 == 0:
                return ans + (ct1 // 3) * 2
            return -1
        else:
            ct1, ct2 = ct2, ct1
            ans = ct2
            ct1 -= ct2
            if ct1 % 3 == 0:
                return ans + (ct1 // 3) * 2
            return -1
