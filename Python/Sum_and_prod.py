import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for i in range(n)], dtype = int)

sumArray = np.sum(arr, axis = 0)
prod = np.product(sumArray)

print(prod)
