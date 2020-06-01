# https://www.hackerrank.com/challenges/itertools-permutations/problem
import itertools

def permutation(s, k):
    s = sorted(s)
    lst = list(itertools.permutations(s, k))
    for i in lst:
        print("".join(i))


if __name__ == '__main__':
    input_lst = input().split()
    string, portion = input_lst[0], int(input_lst[1])
    permutation(string, portion)