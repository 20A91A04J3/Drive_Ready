class Solution:
    def smallestSubstring(self, S):
        # Code here
        zero=False
        one=False
        two=False
        zi=0;oi=0;ti=0
        lenn=99999999
        for i in range(len(S)):
            if(S[i]=='0'):
                zero=True
                zi=i
            elif(S[i]=='1'):
                one=True
                oi=i
            else:
                two=True
                ti=i
            if(zero and one and two):
                lenn=min(lenn,max(oi,zi,ti)-min(oi,zi,ti)
        if(lenn==99999999): return -1
        return lenn
