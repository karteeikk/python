#public modifier
class stud:
    def __init__(self):
        self._name="kartik"
a=stud()
print(a._name)

#private modifier
class emp:
    def __init__(self):
        self.__salary=89000
s=emp()
print(s._emp__salary)
print(s.__dir__())

#protected modifier
class parent:
    def __init__(self):
        self._sname="harry"
    def funcho(self):
        return "code with md"
class child(parent):
    pass
a1=child()
b2=parent()
print(a1._sname)
print(a1.funcho())
print(b2._sname)
print(b2.funcho())