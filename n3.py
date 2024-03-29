import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr.sum(axis=0))
print(arr.sum(axis=1))
print(arr.T)
print(arr.flat)
for item in arr.flat:
    print(item)
print(arr.nbytes)