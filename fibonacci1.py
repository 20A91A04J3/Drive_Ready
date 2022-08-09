a=0
b=1
n=int(input())
n-=2
while(n):
    c=a+b
    a,b=b,c
    n-=1
print(c)
    
