# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy as np

if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = []
    for i in range(m):
        arr.extend(list(map(int, input().split())))

    array = np.array(arr)
    array = array.reshape(m, n)
    transpose = array.transpose()
    flatten = array.flatten()
    print(transpose)
    print(flatten)

# One liner solution
# print("".join([str(i.transpose()) + "\n" + str(i.flatten()) for i in [__import__('numpy').array([list(map(int, input().split())) for _ in range(int(input().split()[0]))])]]))
