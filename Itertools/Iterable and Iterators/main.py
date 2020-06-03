# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
import itertools


def find_probability(s, n, k):
    c = 0
    lst = list(itertools.combinations(range(n), k))

    for i in lst:
        for j in i:
            if s[j] == 'a':
                c += 1
                break

    return c / len(lst)


if __name__ == '__main__':
    N = int(input())
    S = input().split()
    K = int(input())
    print("{:.4f}".format(find_probability(S, N, K)))
