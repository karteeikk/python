class imp:
    name="kartik"
    def __len__(self):
        i=0
        for i in self.name:
            i+=1
        return i
a1=imp()
print(a1.name)
print(len(a1.name))
