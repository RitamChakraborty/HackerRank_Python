# https://www.hackerrank.com/challenges/np-arrays/problem
import numpy


def arrays(array):
    array = numpy.array(array, dtype=float)
    array = numpy.flip(array)
    return array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
