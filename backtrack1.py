def dig(n):
    if (n==0):
        return 0
    return 1+dig(n//10)
print(dig(1234))

    
