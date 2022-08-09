import math
a=int(input())
cnt=0
x=int(math.sqrt(a))
for i in range(1,x+1):
    if (a%i==0):
        x=a//i
        if (i!=x and i%2==x%2):
            cnt+=1
print(cnt)
