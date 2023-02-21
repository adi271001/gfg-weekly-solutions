import math
class Solution:
    def longestSubarray(self, a, b):
        # code here
        num=math.gcd(a,b)
        a=a//num
        b=b//num
        if (a<b):
            t=a
            a=b
            b=t
        ans=1
        x=math.gcd(a,b)
        a-=x
        ans+=a//b
        if (a%b==0 and a>0):
            ans-=1
        return ans
