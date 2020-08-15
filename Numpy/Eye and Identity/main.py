# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy as np

if __name__ == '__main__':
    m, n = map(int, input().split())
    a = np.eye(m, n)
    np.set_printoptions(sign=" ")
    print(a)
