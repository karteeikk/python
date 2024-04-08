n=input("enter a n : ")
try:
    for i in range(1,11):
        print(f"{int(n)} x {i} = {int(n)*i}")
except ValueError:
    print("value must be int")
'''except:
    print("invalid error")
except Exception as e:
    print(e)'''

print("ready to given table")