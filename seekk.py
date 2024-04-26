with open("mysekk.txt","r") as m:
    print(type(m))
    m.seek(10)
    print(m.tell()) #it returns to seek value
    data=m.read(5)
    print(data)