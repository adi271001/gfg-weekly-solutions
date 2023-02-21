class Solution:
    def minimumOperations(self, n, arr):
        # code here
        ma=max(arr)
        li=[]
        for i in range(1,n):
            if (arr[i]==arr[i-1] and arr[i]==ma):
                li.append(i)
        nli=[]
        c=0
        i=0
        for j in range(n):
            if (i!=len(li) and li[i]==j):
                nli.append(c)
                c=0
                i+=1
            elif arr[j]!=ma:
                c+=1
        nli.append(c)
        ans=0
        for i in nli:
            ans+=i//2+i%2
        return ans
