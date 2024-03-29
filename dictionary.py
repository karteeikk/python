thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
print(thisdict)
print(thisdict["year"])
thisdict["color"]="red"
print(thisdict)

x1=thisdict.keys()
x2=thisdict.values()
print(x1)
print(x2)

thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)


