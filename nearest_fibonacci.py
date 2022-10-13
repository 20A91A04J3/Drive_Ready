def fab(n):
    a=0
    b=1
    while True:
        if n==a or n==b:
            return n
        if a>n or b>n:
            if (abs(n-a))>(abs(n-b)):
                return b
            elif(abs(n-a))==(abs(n-b)):
                print(a,end=' ')
                return b
            else:
                return a
        c=a+b
        a=b
        b=c
n=int(input())
res=fab(n)
print(res)
