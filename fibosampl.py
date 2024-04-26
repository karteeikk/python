'''n=int(input("enter an integer : "))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c)'''
n = int(input("enter n:"))
n1=0
n2=1 #use for start with 0
for i in range(1,n+1):
    fibonacci=n1+n2
    print(fibonacci)
    n1=n2
    n2=fibonacci