a={1,2,3,4,5}
b={4,5,6,7,8}

c=a.union(b)
print(c)

a.update(b)
print(a)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 
print(z)
x.intersection_update(y)
print(x)

print(z)

f={2,3,4}
g={2,5,6}
e=f.symmetric_difference(g)  
print(e)
print(f)
f.symmetric_difference_update(g)
print(f)

r={1,2,3,4}
k={2,3,7,8}
l=r.difference(k)    #a-b
print(l)
r.difference_update(k)
print(r)

ko={1,2,3}
ok={4,5,6}
qwe=ko.isdisjoint(ok)   #not a intersection b
print(qwe)

yu={1,2,3,4,5}
uy={9,7,8}
ty={3,4}
uiu=yu.issuperset(uy)
print(uiu)
uio=ty.issubset(yu)
print(uio)
uie=ty.issubset(yu)
print(uie)

yrt={12,434,"krthh",434}
if 12 in yrt:
    print("yes")
else:
    print("no")