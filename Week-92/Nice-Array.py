class Solution:
    def niceSubarray(self, n, arr):
        # code here
        count=1
        ans=0
        for i in range(n):
            if (count==arr[i]):
                count+=1
                ans=max(ans,count-1)
            else:
                count=1
        return ans
