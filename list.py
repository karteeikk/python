temp=[1,2.3,'j','geeta']
print(temp)
print(temp[2])

#perticular range print on temp values

temp=[1,2.3,43,'d','saddsad']
print(temp[-4:-1])
if "saddsad" in temp:
    print("yes")

lis=[]
print([lis*lis for lis in range(10) if lis%2==0])   #list comrehension
