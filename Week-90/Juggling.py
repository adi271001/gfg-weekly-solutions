class Solution:
    def juggling(self, n, li):
        # code here
        ball=[0]*3
        win=[0]*3
        for ba in range(3):
            ball=[0]*3
            ball[ba]=1
            for i in range(n):
                if (ball[li[i][0]-1]==1):
                    ball[li[i][1]-1]=1
                    ball[li[i][0]-1]=0
                elif (ball[li[i][1]-1]==1):
                    ball[li[i][0]-1]=1
                    ball[li[i][1]-1]=0
                if (ball[li[i][2]-1]==1):
                    win[ba]+=1
        mi=0
        ba=0
        for i in range(3):
            if (win[i]>mi):
                mi=win[i]
                ba=i+1
        ans=[ba,mi]
        return ans
