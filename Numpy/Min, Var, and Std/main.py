# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    np.set_printoptions(legacy='1.13')
    array = np.array([list(map(int, input().split())) for _ in range(n)])
    print(np.mean(array, axis=1))
    print(np.var(array, axis=0))
    print(np.std(array, axis=None, dtype=float))
