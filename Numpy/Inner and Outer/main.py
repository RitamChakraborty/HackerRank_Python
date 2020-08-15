# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
import numpy as np

if __name__ == '__main__':
    a1 = np.array(list(map(int, input().split())))
    a2 = np.array(list(map(int, input().split())))
    print(np.inner(a1, a2))
    print(np.outer(a1, a2))
