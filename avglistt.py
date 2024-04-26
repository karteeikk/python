n=int(input("enter size of list : "))
list=[]
for i in range(n):
    e=int(input())
    list.append(e)
add=sum(list)
avarage=add/len(list)
print(avarage)   