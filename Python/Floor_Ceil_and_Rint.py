import numpy as np

np.set_printoptions(sign = " ")

arr = np.array(input().split(), dtype = float)

f = np.floor(arr)
c = np.ceil(arr)
r = np.rint(arr)

print(f)
print(c)
print(r)
