import numpy as np
arr=np.array([1,82,34,30,5])
print(arr)
print(type(arr))
x=np.mean(arr)
print(x)
y=np.median(arr)
print(y)
arr1=np.arange(9)
print(arr1)
print(arr.shape)
print(arr.dtype)
arr[1]=80
print(arr)