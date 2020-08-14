# https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy as np

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    array = np.array(arr)
    array = array.reshape(3, 3)
    print(array)
