def avrage(*n):
    sum=0
    for i in n:
        sum=sum+i
    print(sum/len(n))
avrage(2,3,4,5)
def avg(a=10,b=10):
    return (a+b)/2
c=avg(10,8)
print(c)

def name(**name):
    print("my name is : ",name["sname"],name["fname"],name["lname"])
    print(type(name))
name(sname="mangukiya",fname="kartik",lname="kiritbhai")