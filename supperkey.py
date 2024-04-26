class parentclass:
    def parent_method(self):
        print("har har mahadev")
class childclass(parentclass):
    def child_method(self):
        print("hello")
        super().parent_method()
child=childclass()
child.child_method()
