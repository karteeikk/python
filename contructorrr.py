#default constructor
class dev:
    def __init__(self):
        print("har har magadev")
dev()

#parameterized constructor
class deatail:
    def __init__(self,n,o):
        self.name=n
        self.occ=o
        print(f"{self.name} is a {self.occ}")
a=deatail("kartik","developer")
b=deatail("jasmi","developer")