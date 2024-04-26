temp=[1,2,3,4,5]
def filters(x):
    return x*x>10
new=list(filter(filters,temp))    #filter(function,argument)
print(new)