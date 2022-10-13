n=int(input())
for i in range(n):
    y,x=map(int,input().split())
    m=y-1
    n=x-1
    if n>m:
        if n%2==0:
            print(((n+1)**2)-m)
        else:
            print((n**2)+m+1)
    else:
        if m%2!=0:
            print(((m+1)**2)-n)
        else:
            print((m**2)+n+1)
    
