class emp:
    compony="infosys"
    def show(self):
        print(f"the name is {self.name} and compony is {self.compony}")
    @classmethod
    def change(cls,ncom):
        cls.compony=ncom
e1=emp()
e1.name="kartik"
e1.show()
e1.change("tesla")
e1.show()
print(e1.compony)