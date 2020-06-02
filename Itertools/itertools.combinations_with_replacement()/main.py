# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
import itertools


def permutation(s, k):
    s = sorted(s)
    lst = list(itertools.combinations_with_replacement(s, k))

    for i in lst:
        print("".join(i))


if __name__ == '__main__':
    input_lst = input().split()
    string, portion = input_lst[0], int(input_lst[1])
    permutation(string, portion)