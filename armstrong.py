#Enter input
n = int(input("Enter 3-digit number : "))
 
sum = 0
i = n
while n > 0:
    temp = n % 10
    sum += temp * temp * temp
    n = n//10
print(sum)
if sum==i:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')