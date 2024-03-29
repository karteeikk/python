i=1
k=65
n=3
while(i<=n):
    m=1
    while(m<=n-i):
        print(" ",end="")
        m=m+1
    j=1
    while(j<=i):
        print(chr(k),end="")
        j=j+1
        k=k+1
    print("\n")
    i=i+1
    
    
