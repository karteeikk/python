class math:
    def __init__(self,no):
        self.no=no
    def addno(self,no2):
        self.no=self.no+no2
    def sum(a,b):                   #static method don't use self keyword
        return a+b
a=math(3)
print(a.no)
a.addno(2)
print(a.no)
print(math.sum(2,3))