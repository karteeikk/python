x=input("enter value : ")
if x=="quit":
    print("this string is quit")
elif int(x)>5 or int(x)<9:
    raise ValueError("they are other string")