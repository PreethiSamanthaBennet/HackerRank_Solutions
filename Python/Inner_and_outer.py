import numpy

arr_1 = numpy.array(input().split(),int)
arr_2 = numpy.array(input().split(), int)

print(numpy.inner(arr_1, arr_2))
print(numpy.outer(arr_1, arr_2))
