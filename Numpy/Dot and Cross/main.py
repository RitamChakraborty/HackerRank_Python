# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
import numpy as np

if __name__ == '__main__':
    n = int(input())
    a1 = np.array([list(map(int, input().split())) for _ in range(n)])
    a2 = np.array([list(map(int, input().split())) for _ in range(n)])
    print(np.dot(a1, a2))
