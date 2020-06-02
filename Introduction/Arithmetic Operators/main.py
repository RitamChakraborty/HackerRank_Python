# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
import operator


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    for i in [operator.add, operator.sub, operator.mul]:
        print(i(a, b))
