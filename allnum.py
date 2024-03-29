import statistics as st
import numpy as np

li = [1, 0, 2, 6,6]
numpyArr = np.array(li)
print("Array : ", numpyArr)
print("Mean ",np.mean(numpyArr))
print("Median ",np.median(numpyArr))
print("Mode ",st.mode(numpyArr))
print("Standard Deviation",np.std(numpyArr))
print("Variance ",np.var(numpyArr))
