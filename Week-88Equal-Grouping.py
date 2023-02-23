import math
class Solution:
    def evenGrouping(self, n, arr):
        # code here
        st=[]
        for i in range(n):
            if (len(st)==0):
                st.append(arr[i])
                continue
            num=st[-1]
            if (int(math.log2(num))==int(math.log2(arr[i]))):
                st.pop()
            else:
                st.append(arr[i])
        return len(st)
