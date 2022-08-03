import math
N=1000005
primes=[1]*N
def Generate_seive():
    primes[0]=0
    primes[1]=0
    x=int(math.sqrt(N))
    for i in range(2,x+1):
        if(prime[i]==1):
            for j in range(i*i,N,i):
                primes[j]=0
                
Generate_seive()
t=int(input())
for _ in range(t):
    n=int(input())
    if (primes[n]==1):
        print('prime')
    else:
        print('not a prime')
    

