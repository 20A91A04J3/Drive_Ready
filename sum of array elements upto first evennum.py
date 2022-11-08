n=int(input())
l1=list(map(int,input().split()))
a=[]
for i in l1:
    if i%2!=0:
        a.append(i)
    else:
        a.append(0)
        break
print(sum(a))
