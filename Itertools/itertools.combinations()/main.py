# https://www.hackerrank.com/challenges/itertools-combinations/problem
import itertools


def permutation(s, k):
    s = sorted(s)

    for i in range(1, k + 1):
        lst = list(itertools.combinations(s, i))

        for j in lst:
            print("".join(j))


if __name__ == '__main__':
    input_lst = input().split()
    string, portion = input_lst[0], int(input_lst[1])
    permutation(string, portion)