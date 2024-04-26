print("dir method")
x=(1,2,3,4)
print(dir(x))
#dir() method use to all methods return
print(x.__iter__)

print("dict method")
class person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.verson=1
p=person("rahul",78000)
print(p.__dict__)

