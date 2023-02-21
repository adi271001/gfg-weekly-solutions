class Solution:
    def splitString(self, n, s):
        li1=[0]*26
        li2=[0]*26
        for i in s:
            li2[ord(i)-97]+=1
        ans=0
        for i in s:
            li2[ord(i)-97]-=1
            li1[ord(i)-97]+=1
            temp=0
            for j in range(26):
                if (li1[j]>0 and li2[j]>0):
                    temp+=1
            ans=max(ans,temp)
        return ans
