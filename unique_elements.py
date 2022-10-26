n=int(input())
m=list(map(int,input().strip().split()))[:n]
for i in range(len(m)):
    if m[i]%2==0:
        flag=True
    else:
        flag=False
        print("False")
        break
if flag==True:
    print("True")
