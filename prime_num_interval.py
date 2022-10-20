n=int(input())
m=int(input())
c=0
a=1
for i in range(n,m+1):
    while a<=i:
        if i%a==0:
            c+=1
        a+=1
    if c==2:
        print(i)
    c=0
    a=1
