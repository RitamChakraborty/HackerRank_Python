# https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    array = np.array([list(map(int, input().split())) for _ in range(n)])
    s1 = np.min(array, axis=1)
    print(np.max(s1))
