import numpy as np

nm = input().split()
n, m = int(nm[0]), int(nm[1])

l = [input().split() for i in range(n)]

arr = np.array(l, dtype = int)
print(np.transpose(arr))
print(arr.flatten())
