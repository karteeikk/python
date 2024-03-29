thisset={"alam","banana","cherry"}
print(thisset)
#access iteam
for x in thisset:
    print(x)
print("banana"in thisset)
thisset.add("orange")
print(thisset)
#thisset.clear()
thisset.discard("alam")
print(thisset)

