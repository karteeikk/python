from functools import reduce

sum=[n for n in range(6)]
#reduce(function,iterable)
result=reduce(lambda x,y:x+y,sum)
print(result)