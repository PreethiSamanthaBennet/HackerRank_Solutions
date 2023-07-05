import numpy as np

n, m = map(int, input().split())

A = np.array([input().split() for i in range(n)], dtype = int)
B = np.array([input().split() for i in range(n)], dtype = int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
