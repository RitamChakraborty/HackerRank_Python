# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy as np

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    array = np.array([list(map(int, input().split())) for _ in range(n)])
    s0 = array.sum(axis=0)
    print(s0.prod())
