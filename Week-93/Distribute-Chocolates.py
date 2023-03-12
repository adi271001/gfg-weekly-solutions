class Solution:
    def maxChocolates(self, n, m, Arr):
        # code here
        max_chocolates = max(arr)
        total_chocolates = sum(arr)
        left, right = 1, max_chocolates
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for x in arr:
                total += x // mid
            if total >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right
