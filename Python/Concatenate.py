import numpy

n, m, p = [int(i) for i in input().split()]

arr_1 = numpy.array([input().split() for i in range(n)], int)
arr_2 = numpy.array([input().split() for j in range(m)], int)

print(numpy.concatenate((arr_1, arr_2), axis = 0))
