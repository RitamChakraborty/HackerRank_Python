# https://www.hackerrank.com/challenges/python-mod-divmod/problem
import math

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    print(a // b)
    print(round(math.fmod(a, b)))
    print(divmod(a, b))
