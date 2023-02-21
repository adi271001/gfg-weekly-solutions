class Solution:
    def maximumPossible(self, n, k, s):
        # code here
        mod=10**9+7
        def binaryexp(a,n):
            res=1
            while(n):
                if (n%2):
                    res=res*a
                    res=res%mod
                a=a*a
                a=a%mod
                n=n//2
            return res
        def fact(n):
            if (n==0):
                return 1
            fct=1
            for i in range(1,n+1):
                fct*=i
                fct=fct%mod
            return fct
        mp=dict()
        for i in range(26):
            mp[chr(97+i)]=0
        for i in s:
            mp[i]+=1
        k=min(n,k)
        for i in range(k):
            machr=0
            ma=0
            michr=0
            mi=10**9
            for j in mp:
                if (mp[j]>ma):
                    ma=mp[j]
                    machr=j
                if (mp[j]<mi):
                    mi=mp[j]
                    michr=j
            mp[machr]-=1
            mp[michr]+=1
        num1=fact(n)
        num2=1
        for i in mp:
            num2*=fact(mp[i])
            num2=num2%mod
        modinv=binaryexp(num2,mod-2)
        ans=num1*modinv
        ans=ans%mod
        return ans
