# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import numpy as np

if __name__ == '__main__':
    shape = tuple(map(int, input().split()))
    zeros = np.zeros(shape, dtype=int)
    ones = np.ones(shape, dtype=int)
    print(zeros)
    print(ones)
