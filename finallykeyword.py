def fun1():
    try:
        temp=[1,2,3,4]
        i=int(input("enter a value of i : "))
        print(temp[i])
        return True
    except:
        print("some error occured")
        return False
    finally:
        print("your answer is this always printed if use fun but not other")
x=fun1()
print(x)