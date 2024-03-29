def temp():
    n=int(input('enter a value : '))
    s=0
    for i in range(1,n+1):
        s=s+i;
    return s;
print('sum of number is',temp())
