thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
for key in thisdict.keys():
    print(thisdict[key])
print(thisdict.items())

for key,value in thisdict.items():
    print(f"the key is {key} of value {value}")
print(thisdict)

#thisdict.clear()
print(thisdict)
x=thisdict.get("model")
print(x)
y=thisdict.copy()
print(y)
