a=5
b=5
print(a is b) #exact location of object in memory
print(a==b)  #value
c="kartik"
d="kartik"
print(c is d)
print(c==d)
e=[1,2,3]
f=[1,2,3]
print(e==f)  #list value is sem
print(e is f) #list value is sem but location of object nd list are unchangable
g=(2,3,4,5)
f=(2,3,4,5) #tuple are unchangable that's true
print(g==f)
print(g is f)

x=None
y=None
print(x is y,x==y)