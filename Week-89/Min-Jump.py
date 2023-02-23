from typing import List
class Solution:
    def minJump(self, n : int, arr : List[int]) -> int:
        # code here
        a=[]
        for i,el in enumerate(arr):
            if el%2==0 or el%3==0:
                a.append(i)
        ans=0
        for c,d in zip(a,a[1:]):
            ans=max(ans,d-c)
        return ans
