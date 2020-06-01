# https://www.hackerrank.com/challenges/itertools-product/problem
import itertools


def product(l1, l2):
    result = itertools.product(l1, l2)
    s = " ".join(map(str, list(result)))
    print(s)


if __name__ == '__main__':
    lst1 = map(int, input().split())
    lst2 = map(int, input().split())
    product(lst1, lst2)
