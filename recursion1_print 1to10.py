for i in range(1,11):
    print(i)
def Display(x):
    if(x>10):
        return
    print(x)
    Display(x+1)
Display(1)
