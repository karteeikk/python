class employee:
    eid=1
    name="kartik"
    gender="male"
    def info(self):   #self parameter used to perticular record iterable
        print(f"{self.name} is {self.gender}")
a=employee()
b=employee()
c=employee()
a.name="jasmi"
a.gender="female"
b.name="om"
b.gender="male"
a.info()
b.info()
c.info()
