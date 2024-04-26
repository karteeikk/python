list=[1,2,3,4,5,6,7]
print(list)
for i in range(1,4):
    list.insert(7,list[0])
    list.pop(0)

print(list)