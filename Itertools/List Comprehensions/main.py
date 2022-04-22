import itertools


if __name__ == '__main__':
    x, y, z, n = map(int, [input() for _ in range(4)])
    lst = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k) != n:
                    lst += [i, j, k]
    
    print(lst)