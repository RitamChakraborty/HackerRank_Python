# https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np

if __name__ == '__main__':
    cofs = np.array(list(map(float, input().split())))
    x = int(input())
    result = np.polyval(cofs, x)
    print(result)
