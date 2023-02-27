from collections import defaultdict
from bisect import bisect_left,bisect_right
class Solution:
    def bestPrice(self,n,price,k,q,queries):
        temp=defaultdict(int)
        min_price=float("inf")
        max_price=-float("inf")
        for low,high in price:
            min_price=min(min_price,low)
            max_price=max(max_price,high+1)
            temp[low]+=1
            temp[high+1]-=1
        t=0
        good_prices=[]
        
        for pric in range(min_price,max_price+1):
            t+=temp[pric]
            if t>=k:
                good_prices.append(pric)
        ans=[]
        for l,r in queries:
            ind1=bisect_right(good_prices,l-1)
            ind2=bisect_right(good_prices,r)
            ans.append(ind2-ind1)
        return ans
