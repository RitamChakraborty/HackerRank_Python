# https://www.hackerrank.com/challenges/np-concatenate/problem
import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a1 = np.array([list(map(int, input().split())) for _ in range(n)])
    a2 = np.array([list(map(int, input().split())) for _ in range(m)])
    a = np.concatenate((a1, a2))
    print(a)
