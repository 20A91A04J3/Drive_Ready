def Is_palin(i,j,s):
    if(i==j):return True
    if(s[i]==s[j]):
        return Is_palin(i+1,j-1,s)
    else:
        return False
s="MCDAM"
print(Is_palin(0,len(s)-1,s))
