n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
for i in range(len(m)):
    if m[i]%2==0:
        if c%2==0:
            flag=True
        else:
            flag=False
            print("False")
            break
    c+=1
if flag==True:
    print('True')
