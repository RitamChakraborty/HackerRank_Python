# https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    a1 = np.array([list(map(int, input().split())) for _ in range(n)])
    a2 = np.array([list(map(int, input().split())) for _ in range(n)])

    print(a1 + a2)
    print(a1 - a2)
    print(a1 * a2)
    print(a1 // a2)
    print(a1 % a2)
    print(a1 ** a2)
