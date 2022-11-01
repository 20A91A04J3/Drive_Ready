n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
b=[]
for i in range(len(m)):
    if m[i] not in b:
        if m[i]%2==0:
            c+=1
        b.append(m[i])
print(c)
