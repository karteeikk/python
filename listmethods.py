fruits=["apple","mango","apple","banana","cherry"]
print(fruits)
fruits.append("orange")    #append
print(fruits)
#fruits.clear()             clear
x=fruits.copy()            #copy
print(x)
x=fruits.count("apple")    #count
print(x)
x=fruits.index("banana")   #index
print(x)
fruits.insert(3,"pineapple")   #insert
print(fruits)
fruits.pop(5)                  #pop
print(fruits)
fruits.remove("mango")        #remove
print(fruits)
fruits.reverse()              #reverse
print(fruits)
cars=['ford','bmw','volvo']
cars.sort()                   #sort
print(cars)
cars.sort(reverse=True)
print(cars)
l=[1,2,3,4,5]
m=[6,7,8,9]
l.extend(m)
print(l)                       #extend