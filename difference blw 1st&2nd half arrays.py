n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
a=n//2
s=0
p=0
for i in range(len(m)):
    c+=1
    if c<=a:
        s=s+m[i]
    else:
        p=p+m[i]
print(abs(s-p))
