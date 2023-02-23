 prev=0
        ans=0
        odd=0
        even=0
        temp=0
        buf=0
        for el in arr:
            if el%2==0:
                ans+=prev
                buf+=1
            else:
                if temp==0:
                    even+=buf+1
                    buf=0
                    temp+=1
                else:
                    if temp%2:
                        ans+=even
                        prev=even
                        odd+=buf+1
                        buf=0
                        temp+=1
                    else:
                        ans+=odd
                        prev=odd
                        even+=buf+1
                        buf=0
                        temp+=1
        return ans
