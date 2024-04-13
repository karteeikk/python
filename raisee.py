temp=int(input("enter value of temp : "))
if temp>5 and temp<9:
    print(temp)
else:
    raise ValueError("value sould be an integer")