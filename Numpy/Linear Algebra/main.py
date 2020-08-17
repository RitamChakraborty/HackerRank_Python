# https://www.hackerrank.com/challenges/np-linear-algebra/problem
import numpy as np

if __name__ == '__main__':
    np.set_printoptions(legacy="1.13")
    matrix = np.array([list(map(float, input().split())) for _ in range(int(input()))])
    det = np.linalg.det(matrix)
    print(det)
