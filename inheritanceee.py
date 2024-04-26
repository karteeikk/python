class employee:
    def __init__(self,id,name):
        self._id=id
        self._name=name
    def show(self):
        print(f"id is {self._id} and name is {self._name}")
class programmer(employee):
    def show1(self):
        print("hey buddy")
e1=employee(1,"kartik")
e1.show()
e2=programmer(2,"meet")
e2.show()
e2.show1()