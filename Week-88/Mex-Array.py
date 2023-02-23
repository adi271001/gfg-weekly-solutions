class Solution:
    def mexArray(self, n, arr):
        # code here
        arr.sort(reverse=True)
        mp=dict()
        ans=[]
        num=0
        for i in range(n):
            mp[arr[i]]=1
            while(True):
                if (num not in mp):
                    ans.append(num)
                    break
                else:
                    num+=1
        return ans
