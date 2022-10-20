n=int(input())
c=0
while True:
    n+=1
    s=str(n)
    a=s[::-1]
    if n==int(a):
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        if c==2:
            print(n)
            break
        c=0
