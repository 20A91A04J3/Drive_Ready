n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=int(input())
s=0
for i in range(len(m)):
    s=s+m[i]
    if m[i]==a:
        break
print(s)
