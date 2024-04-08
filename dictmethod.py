temp={"raj":30,"mohan":70,"kishan":89}
temp1={"rishi":90,"shruti":28}
print(temp)

temp.update(temp1)
print(temp)

temp.pop("raj")
print(temp)

temp.popitem()
print(temp)

#del temp
#print(temp)
#temp.clear()
#print(temp)
for keys,values in temp.items():
    print(f"this is key {keys} and this is value {values}")