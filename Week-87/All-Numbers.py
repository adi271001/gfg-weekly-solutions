class Solution:
    def allNumbers(self, a, b):
        # code here
        li=[]
        for i in range(a,b+1,a):
            if (b%i==0):
                li.append(i)
        return li
