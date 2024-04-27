class shap:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def midd(self):
        return self.x*self.y
    
class circle(shap):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c1=shap(2,3)
print(c1.midd())

c=circle(5)
print(c.area())