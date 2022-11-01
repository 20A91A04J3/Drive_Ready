n=int(input())
l=list(map(int,input().split()))
l=set(l)
a=[]
for i in l:
    if i%2!=0:
        a.append(i)
print(len(a))
    
